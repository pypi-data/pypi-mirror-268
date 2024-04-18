import itertools
import logging
from functools import wraps as _wraps

from . import utils as _utils

_logger = logging.getLogger(__name__)


def _unstable(func):
    @_wraps(func)
    def result(*args, **kwargs):
        _logger.warning(
            'Pipeline %s is experimental and unstable, it may break your level. Consider remove this pipeline.',
            func.__name__
        )
        return func(*args, **kwargs)

    return result


UNWIND_TAG_EVENT_ACTION_TYPE: dict[str, str] = {
    'RunAll': 'Run',
    'EnableAll': 'Enable',
    'DisableAll': 'Disable',
}


def unwind_tags(level: dict):
    """
    Replaces all RunAll, EnableAll and DisableAll tag invocations
    with iterative Run, Enable and Disable tag invocations.

    :param level: Level as a json object in a dict.
    :return:
    """
    tags = list(map(lambda x: x.get('tag'), level['events']))

    new_events = []
    for event in level['events']:
        if event['type'] != 'TagAction' or event['Action'] not in UNWIND_TAG_EVENT_ACTION_TYPE:
            new_events.append(event)
            continue

        event['Action'] = UNWIND_TAG_EVENT_ACTION_TYPE[event['Action']]
        for name in filter(lambda x: event['Tag'] in x, tags):
            new_event = event.copy()
            new_event['Tag'] = name
            new_events.append(new_event)

    level['events'] = new_events


def rename_tags(level: dict):
    """
    Rename all event tags in the level to random names.

    :param level: Level as a json object in a dict.
    :return:
    """
    unwind_tags(level)

    name_mapping = {}
    for event in level['events']:
        if 'tag' in event:
            event['tag'] = _utils.dict_get_random_name(name_mapping, event['tag'], 16)

        if event['type'] == 'TagAction':
            event['Tag'] = _utils.dict_get_random_name(name_mapping, event['Tag'], 16)


def shuffle_events(level: dict):
    """
    Shuffle all events with respect to file order in the level.
    Events executing order will be maintained.

    :param level: Level as a json object in a dict.
    :return:
    """
    grouped_events = [list(x[1])[::-1] for x in itertools.groupby(level['events'], key=lambda x: (x['bar'], x['beat']))]
    new_events = []
    while len(grouped_events) > 0:
        index = _utils.random.randint(0, len(grouped_events) - 1)
        new_events.append(grouped_events[index].pop())
        if len(grouped_events[index]) == 0:
            grouped_events.pop(index)

    level['events'] = new_events


def remove_comments(level: dict):
    """
    Remove all comments in the level.

    :param level: Level as a json object in a dict.
    :return:
    """
    level['events'] = list(
        filter(lambda x: x['type'] != 'Comment' or x['text'].strip().startswith('()=>'), level['events'])
    )


def hide_comments(level: dict):
    """
    Hide all comments in the level,
    i.e. not showing when playing in the editor.

    :param level: Level as a json object in a dict.
    :return:
    """
    for event in level['events']:
        if event['type'] == 'Comment':
            event['show'] = False


MOVE_Y_BLACKLIST_TYPE = ['MoveRoom', 'SetRoomContentMode', 'MaskRoom', 'FadeRoom', 'SetRoomPerspective']
MOVE_Y_RANGE = range(-4096, 4096)


def move_y(level: dict):
    """
    Randomize all y values for every event in the level.
    Does not randomize y values for events in MOVE_Y_BLACKLIST_TYPE.

    :param level: Level as a json object in a dict.
    :return:
    """
    for event in level['events']:
        if event['type'] in MOVE_Y_BLACKLIST_TYPE or 'y' not in event:
            continue

        event['y'] = _utils.random.choice(MOVE_Y_RANGE)


def remove_bookmarks(level: dict):
    """
    Remove all bookmarks in the level.

    :param level: Level as a json object in a dict.
    :return:
    """
    level['bookmarks'] = []


def rename_conditionals(level: dict):
    """
    Rename all conditionals in the level to random names.

    :param level: Level as a json object in a dict.
    :return:
    """
    name_mapping = {}
    for condition in level['conditionals']:
        condition['name'] = ''
        condition['tag'] = _utils.dict_get_random_name(name_mapping, condition['tag'], 16)


def shuffle_conditionals(level: dict):
    """
    Shuffle all conditionals in the level.

    :param level: Level as a json object in a dict.
    :return:
    """
    _utils.random.shuffle(level['conditionals'])


DEEPEN_EVENTS_PROBABILITY = 0.05
DEEPEN_EVENTS_BLACKLIST_TYPE = [
    'PlaySong',
    'SetBeatsPerMinute',
    'SetClapSounds',
    'SetBeatSound',
    'SetCrotchetsPerBar',
    'PlaySound',
    'SetCountingSound',
    'SetGameSound',
    'SayReadyGetSetGo',

    'AddOneshotBeat',
    'SetOneshotWave',
    'AddClassicBeat',
    'SetRowXs',
    'AddFreeTimeBeat',
    'PulseFreeTimeBeat',
]


@_unstable
def deepen_events(level: dict):
    """
    Deepen all events in the level by adding anchor tag invocations.
    Does not deepen events in DEEPEN_EVENTS_BLACKLIST_TYPE.
    This pipeline is unstable and may break your level.

    :param level: Level as a json object in a dict.
    :return:
    """
    events: list[dict] = level['events'][::-1]
    new_events = []
    cnt = 0

    while len(events) > 0:
        event = events.pop()
        if event['type'] in DEEPEN_EVENTS_BLACKLIST_TYPE or _utils.random.random() >= DEEPEN_EVENTS_PROBABILITY:
            new_events.append(event)
            continue

        anchor_tag = f'__event_anchor_{cnt}'
        cnt += 1
        anchor = {
            'bar': event['bar'],
            'beat': event['beat'],
            'type': 'TagAction',
            'Action': 'Run',
            'Tag': anchor_tag,
        }
        if 'y' in event:
            anchor['y'] = event['y']
        if 'tag' in event:
            anchor['tag'] = event['tag']
        event['tag'] = anchor_tag

        events.append(event)
        events.append(anchor)

    level['events'] = new_events


def move_tags(level: dict):
    """
    Move all tagged events in the level to random positions.
    Events' order with the same tag will be maintained.

    :param level:
    :return:
    """
    beats_per_bar = _utils.beats_per_bar_list(level['events'])
    total_beats = sum(beats_per_bar[1:])

    tag_start_offset = {
        event['tag']: _utils.find_event_offset(beats_per_bar, event['bar'], event['beat']) for event in
        (min(events, key=lambda x: (x['bar'], x['beat'])) for tag, events in
         itertools.groupby(filter(lambda x: 'tag' in x, level['events']), lambda x: x['tag']))
    }
    tag_new_start_offset = {}

    for event in level['events']:
        if 'tag' not in event:
            continue

        start = tag_start_offset[event['tag']]
        new_start = tag_new_start_offset.setdefault(event['tag'], _utils.random.random() * total_beats)
        delta = new_start - start
        new_offset = _utils.find_event_offset(beats_per_bar, event['bar'], event['beat']) + delta
        new_bar, new_beat = _utils.find_event_position(beats_per_bar, new_offset)

        event['bar'] = new_bar
        event['beat'] = new_beat
