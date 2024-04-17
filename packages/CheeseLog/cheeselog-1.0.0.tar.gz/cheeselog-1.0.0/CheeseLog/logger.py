import inspect, datetime, sys, re, os, multiprocessing, time, queue
from typing import Dict, Set
from multiprocessing.synchronize import Event

import setproctitle

from CheeseLog import style
from CheeseLog.level import Level

class Logger:
    def __init__(self):
        self.messageTemplate: str = '(%l) %t > %c'
        self.styledMessageTemplate: str = '(<black>%l</black>) <black>%t</black> > %c'
        self.timerTemplate: str = '%Y-%m-%d %H:%M:%S.%f'
        self.levels: Dict[str, Level] = {
            'DEBUG': Level(10),
            'INFO': Level(20, styledMessageTemplate = '(<green>%l</green>) <black>%t</black> > %c'),
            'STARTING': Level(20, styledMessageTemplate = '(<green>%l</green>) <black>%t</black> > %c'),
            'ENDING': Level(20, styledMessageTemplate = '(<green>%l</green>) <black>%t</black> > %c'),
            'LOADING': Level(20, styledMessageTemplate = '(<blue>%l</blue>) <black>%t</black> > %c'),
            'LOADED': Level(20, styledMessageTemplate = '(<cyan>%l</cyan>) <black>%t</black> > %c'),
            'HTTP': Level(20, styledMessageTemplate = '(<blue>%l</blue>) <black>%t</black> > %c'),
            'WEBSOCKET': Level(20, styledMessageTemplate = '(<blue>%l</blue>) <black>%t</black> > %c'),
            'WARNING': Level(30, styledMessageTemplate = '(<yellow>%l</yellow>) <black>%t</black> > %c'),
            'DANGER': Level(40, styledMessageTemplate = '(<red>%l</red>) <black>%t</black> > %c'),
            'ERROR': Level(50, styledMessageTemplate = '(<magenta>%l</magenta>) <black>%t</black> > %c')
        }

        self.weightFilter: int = 0
        self.levelFilter: Set[str] = set()
        self.moduleFilter: Dict[str, int | Set[str]] = {}
        self.contentFilter: Set[re.Match] = set()
        self.logger_weightFilter: int = 0
        self.logger_levelFilter: Set[str] = set([ 'LOADING' ])
        self.logger_moduleFilter: Dict[str, int | Set[str]] = {}
        self.logger_contentFilter: Set[re.Match] = set()

        self.styled: bool = True

        self._filePath: str = ''
        self.fileExpire: datetime.timedelta = datetime.timedelta(seconds = 0)

        self._processHandler: multiprocessing.Process | None = None
        self._event: Event = multiprocessing.Event()
        self._queue: multiprocessing.Queue = multiprocessing.Queue()

    def _processHandle(self):
        setproctitle.setproctitle(setproctitle.getproctitle() + ':CheeseLog')

        while not self._event.is_set():
            try:
                if self.fileExpire.total_seconds():
                    try:
                        fileExpire = (datetime.datetime.now() - self.fileExpire).strftime(self.filePath)
                        os.remove(fileExpire)
                    except:
                        ...

                data = self._queue.get()
                message = data[2].strftime(data[3].replace('%l', data[0]).replace('%c', data[1]).replace('%t', data[4])).replace('\n', '\n    ').replace('&lt;', '<').replace('&gt;', '>') + '\n'

                try:
                    filePath = time.strftime(self.filePath)
                except:
                    filePath = self.filePath

                os.makedirs(os.path.dirname(filePath), exist_ok = True)
                with open(filePath, 'a', encoding = 'utf-8') as f:
                    f.write(message)
            except KeyboardInterrupt:
                ...

    def default(self, level: str, message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False):
        if level not in self.levels:
            raise KeyError('No level with this key')

        if self.levels[level].weight < self.weightFilter:
            return

        if level in self.levelFilter:
            return

        if self.moduleFilter:
            stack = inspect.stack()
            for key, value in self.moduleFilter.items():
                flag = False
                for frame in stack:
                    callingModule = frame.frame.f_locals.get('__name__')
                    if callingModule and callingModule == key:
                        flag = True
                        if isinstance(value, int):
                            if self.levels[level].weight <= value:
                                return
                        elif isinstance(value, Set):
                            if level in value:
                                return
                        break
                if flag:
                    break

        for pattern in self.contentFilter:
            if re.search(pattern, message):
                return

        now = datetime.datetime.now()
        message = str(message)
        if sys.stdout and sys.stdout.isatty():
            if self.styled:
                _message = re.sub(r'<.+?>', lambda s: '\033[' + getattr(style, s[0][1:-1].upper())[0] + 'm', re.sub(r'</.+?>', lambda s: '\033[' + getattr(style, s[0][2:-1].upper())[1] + 'm', now.strftime((self.levels[level].styledMessageTemplate or self.styledMessageTemplate).replace('%l', level).replace('%c', styledMessage or message).replace('%t', self.timerTemplate)))).replace('\n', '\n    ')
            else:
                _message = now.strftime((self.levels[level].messageTemplate or self.messageTemplate).replace('%l', level).replace('%c', message).replace('%t', self.timerTemplate)).replace('\n', '\n    ')
            if refreshed:
                _message = '\033[F\033[K' + _message
            print(_message.replace('&lt;', '<').replace('&gt;', '>'), end = end)

        if not self.filePath:
            return

        if self.levels[level].weight < self.logger_weightFilter:
            return

        if level in self.logger_levelFilter:
            return

        if self.logger_moduleFilter:
            for key, value in self.logger_moduleFilter.items():
                flag = False
                for frame in stack:
                    callingModule = frame.frame.f_locals.get('__name__')
                    if callingModule and callingModule == key:
                        flag = True
                        if isinstance(value, int):
                            if self.levels[level].weight <= value:
                                return
                        elif isinstance(value, Set):
                            if level in value:
                                return
                        break
                if flag:
                    break

        for pattern in self.logger_contentFilter:
            if re.search(pattern, message):
                return

        self._queue.put((level, message, now, self.levels[level].messageTemplate or self.messageTemplate, self.timerTemplate))

    def debug(self, message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False):
        self.default('DEBUG', message, styledMessage, end = end, refreshed = refreshed)

    def info(self, message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False):
        self.default('INFO', message, styledMessage, end = end, refreshed = refreshed)

    def starting(self, message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False):
        self.default('STARTING', message, styledMessage, end = end, refreshed = refreshed)

    def ending(self, message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False):
        self.default('ENDING', message, styledMessage, end = end, refreshed = refreshed)

    def warning(self, message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False):
        self.default('WARNING', message, styledMessage, end = end, refreshed = refreshed)

    def danger(self, message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False):
        self.default('DANGER', message, styledMessage, end = end, refreshed = refreshed)

    def error(self, message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False):
        self.default('ERROR', message, styledMessage, end = end, refreshed = refreshed)

    def websocket(self, message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False):
        self.default('WEBSOCKET', message, styledMessage, end = end, refreshed = refreshed)

    def http(self, message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False):
        self.default('HTTP', message, styledMessage, end = end, refreshed = refreshed)

    def loaded(self, message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False):
        self.default('LOADED', message, styledMessage, end = end, refreshed = refreshed)

    def loading(self, message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = True):
        self.default('LOADING', message, styledMessage, end = end, refreshed = refreshed)

    def encode(self, message: str) -> str:
        return message.replace('<', '&lt;').replace('>', '&gt;').replace('%', '%%')

    def destroy(self):
        self._event.set()
        self._processHandler.terminate()
        self._processHandler.join()
        self._event.clear()
        self._processHandler = None

    @property
    def filePath(self) -> str:
        return self._filePath

    @filePath.setter
    def filePath(self, value: str):
        self._filePath = value

        if self.filePath and not self._processHandler:
            self._processHandler = multiprocessing.Process(target = self._processHandle, name = setproctitle.getproctitle() + ':CheeseLog')
            self._processHandler.start()
        elif not self.filePath and self._processHandler:
            self._event.set()
            self._processHandler.join()
            self._event.clear()
            self._processHandler = None

logger = Logger()
