"""BreakPoint implements a debugging tool consisting of an interactive
session."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os
import subprocess
import sys

from icecream import ic
from vistutils.parse import maybe
from vistutils.text import monoSpace, stringList

from typing import Any

if sys.version_info.minor < 11:
  from typing_extensions import Self
else:
  from typing import Self


class BreakPoint:
  """BreakPoint implements a debugging tool consisting of an interactive
  session."""
  __active_state__ = None

  __focus_object__ = None
  __next_command__ = None
  __current_lines__ = None
  __clipped_lines__ = None
  __latest_input__ = None
  __file_name__ = None
  __fallback_file_name__ = '_temp.py'

  def __init__(self, focusObject: object = None) -> None:
    self.setFocusObject(focusObject)

  def setFocusObject(self, focusObject: object) -> None:
    """Setter-function for the focus object"""
    self.__focus_object__ = focusObject

  def getFocusObject(self, ) -> object:
    """Getter-function for the focus object"""
    return self.__focus_object__

  def __rrshift__(self, other: object) -> Self:
    """Right shift operator"""
    self.setFocusObject(other)
    return self

  @staticmethod
  def getDefaultEditor() -> str:
    """Getter-function for the default editor"""
    return os.environ.get('EDITOR', None)

  @staticmethod
  def validate(editor: str) -> bool:
    """Validates the editor"""
    editors = ['vi', 'nano', 'emacs', 'gedit', 'kate', 'code', 'sublime', ]
    if editor not in editors:
      return False
    res = subprocess.run(['which', editor], capture_output=True)
    return False if res.returncode else True

  @staticmethod
  def getAvailableEditors() -> list[str]:
    """Getter-function for the available editors"""
    out = []
    editors = ['vi', 'nano', 'emacs', 'gedit', 'kate', 'code', 'sublime', ]
    for editor in editors:
      res = subprocess.run(['which', editor], capture_output=True)
      if not res.returncode:
        out.append(editor)
    return out

  @staticmethod
  def _getUsage() -> str:
    """Getter-function for the usage string"""

    usage = """<tab>Insert any code to run from here. Enter as many lines 
    as needed. To proceed, send an empty line. The prompt will then you 
    the code you have entered. If you are satisfied, give the input: 'RUN'
    and the code will run. Any other input will return you to code edit 
    mode.<br><br><tab>

    In edit mode, the lines of codes are numbered sequentially. To copy 
    the current content at lines 2, 3 and 4 into the clipboard, issue:
    '2yy4'. Alternatively, use '2dd4' to cut the lines also bringing the 
    contents to the clipboard but also removing the lines. Line 5 falls 
    to line 2 and so one. To paste lines into the code, so that the 
    first line appears at line 7, issue '7pp'. This will insert lines at 
    line.<br><br><tab>

    You can save your debug inspections by issuing: :wq [fileName] This 
    will allow you to reuse those commands. If necessary, you may wish 
    to use an actual editor to setup some commands. Fortunately, you can 
    issue: :vi [fileName] which opens the named file in vi. If no file 
    name is specified, vi  will open a temp file with the current 
    content allowing for external edits. Please note that changing the 
    filename will remove the current contents. To save the file in vi, 
    use: :wq. To exit without saving, use: :q!. <br><br><tab>

    The external edits are facilitated by invoking 'subprocess.run'. 
    This grants access to the system shell, allowing for the use of any 
    editor available on the system. Please note, that because of the use 
    the run function, the python code cannot proceed until the editor 
    closes. A future version is planned to have a feature allowing for a 
    Popen to be used instead.  <br><br><tab>

    To exit this interactive session, issue :q or exit() or exit."""

    return monoSpace(usage)

  @staticmethod
  def _getNormalPrompt() -> str:
    """Getter-function for the normal prompt"""

    msg = """Awaiting input. Issue a blank line to enter CODE MODE, 
    or one of the following: <br>
    <tab> :vi [fileName (optional)] open the code externally in the 
    editor at environment variable: EDITOR, currently set to: %s. (It 
    doesn't actually start up 'vi'). Please note that the python 
    script will remain interrupted whilst the external editor is 
    running. To return from the external editor, simply exit the 
    editor, for example in vi by saving with :wq. In this case, 
    the code is saved to the fileName which defaults to the temp file.<br>
    <tab> :q to exit the interactive session. <br>
    <tab> exit to exit the interactive session. <br> """
    return monoSpace(msg % os.environ.get('EDITOR', 'vi'))

  @staticmethod
  def _getCodePrompt() -> str:
    """Getter-function for the code prompt"""
    msg = """During CODE MODE, input code lines to build up the the 
    script. Hit enter to append the current line to the code lines. Give 
    an empty line to return to NORMAL MODE. """
    return monoSpace(msg)

  @staticmethod
  def _getHeader() -> str:
    """Getter-function for the header"""
    return monoSpace('--<|  Welcome to WaitAMinute!  |>--'.center(75, '-'))

  @staticmethod
  def _getModeHeader(mode: str) -> str:
    """Getter-function for the mode header"""
    modeHeader = ']>-%s-<[' % ('| %s |'.center(69, ' ')) % mode.upper()
    return monoSpace(modeHeader)

  def deactivate(self) -> None:
    """Deactivates the breakpoint"""
    self.__active_state__ = False

  def __bool__(self, ) -> bool:
    """Returns True if the breakpoint should still hold the loop"""
    return True if self.__active_state__ else False

  @staticmethod
  def _runCode(code: str) -> None:
    """Runs the code"""
    exec(code)

  @staticmethod
  def _parseFile(fileName: str) -> str:
    """Parses the file"""
    if fileName is None:
      fileName = 'temp.py'
    here = os.path.dirname(os.path.abspath(__file__))
    if not os.path.isabs(fileName):
      fileName = os.path.basename(fileName)
      fileName = os.path.join(here, fileName)
    return fileName

  def _getFileName(self) -> str:
    """Getter-function for file name"""
    return maybe(self.__file_name__, self.__fallback_file_name__)

  def _setFileName(self, fileName: str) -> str:
    """Setter-function for file name"""
    baseName = os.path.basename(fileName)
    name, ext = os.path.splitext(baseName)
    if os.path.isabs(fileName):
      dirName = os.path.dirname(fileName)
      self.__file_name__ = os.path.join(dirName, '%s.py' % name)
      return fileName
    self.__file_name__ = '%s.py' % name
    return fileName

  def _saveCode(self, fileName: str = None) -> None:
    """Saves the code"""
    fileName = self._getFileName() if fileName is None else fileName
    codeLines = self.getCodeLines()
    codeFile = '\n'.join(codeLines)
    with open(self._parseFile(fileName), 'w', encoding='utf-8') as f:
      f.write(codeFile)

  def _loadCode(self, fileName: str = None) -> str:
    """Loads the code"""
    fileName = self._getFileName() if fileName is None else fileName
    with open(self._parseFile(fileName), 'r', encoding='utf-8') as f:
      return f.read()

  def _yankLines(self, start: int, end: int) -> None:
    """Yanks the lines"""
    self.__clipped_lines__ = [*self.getCodeLines()[start:end], ]

  def _yeetLines(self, start: int, end: int) -> None:
    """Yeets the lines"""
    self.__clipped_lines__ = []
    for i in range(start, end):
      self.__clipped_lines__.append(self.getCodeLines().pop(start))
      #  Please note, that: pop(start) is correct, because after each pop
      #  the next line has moved up to start index.

  def pasteLines(self, start: int) -> None:
    """Pastes the lines"""
    self.__current_lines__.insert(start, *self.__clipped_lines__)

  def getCodeLines(self, ) -> list[str]:
    """Getter-function for the current list of code lines."""
    if self.__current_lines__ is None:
      self.__current_lines__ = []
    return self.__current_lines__

  def externalEdit(self, *args, **kwargs) -> None:
    """External edit"""
    fileNameKeys = stringList("""fileName, file, name, fid, f, n""")
    editorKeys = stringList("""editor, edit, e""")
    fileName, editor = None, None
    for (key, val) in kwargs.items():
      if key in fileNameKeys and fileName is None:
        fileName = val
      if key in editorKeys and editor is None:
        if editor in self.getAvailableEditors():
          editor = val

    fileName = self._parseFile(fileName)
    subprocess.run(['vi', fileName])

  def promptLoop(self, ) -> None:
    """Input loop for the breakpoint"""
    header = '--<|  Welcome to WaitAMinute!  |>--'.center(75, '-')
    print(self._getUsage())
    while self:
      header = '|>-%s-<|' % header
      subprocess.run(['clear'])
      print(self._getUsage())
      print(']>-%s-<[' % ('| Wait A Minute! |'.center(69, ' ')))
      lines = self.getCodeLines()
      for (i, line) in enumerate(lines):
        codeLine = '%02d  |%s' % (i, line)
        print('%s|' % codeLine.ljust(77, ' '))

  @staticmethod
  def exitPrompt() -> str:
    """Exit prompt"""
    msg = """Please inspect the code. When ready, issue 'RUN' to run the 
    code. Alternatively, issue any other command to return. """
    print(monoSpace(msg))
    return input(']>-Ready? Then say: RUN-<[')

  def appendLine(self, line: str) -> str:
    """Appends a line to the code"""
    self.getCodeLines().append(line)
    return line

  def getLatestInput(self, ) -> str:
    """Getter-function for the latest input"""
    return self.__latest_input__

  def setLatestInput(self, latestInput: str) -> str:
    """Setter-function for the latest input"""
    self.__latest_input__ = latestInput
    return latestInput

  def runCode(self, ) -> Any:
    """Runs the code"""
    raise NotImplementedError

  @staticmethod
  def _validateNormalCommand(cmd: str = None) -> bool:
    """Validates the command"""
    return True if cmd in ['exit', ':q', ':vi', ':w', ] else False

  def __call__(self, cmd: str = None) -> None:
    """Activates the breakpoint"""
    cmd = 'NORMAL' if cmd is None else cmd
    cmd = cmd or 'CODE'
    print(self._getHeader())
    if cmd not in ['CODE', 'NORMAL']:
      if cmd[0] == ':':
        op, arg = [*cmd.split(' '), None][:2]
      else:
        cmd = input('Invalid command! Please a valid command.')
        return self(cmd)
      if op == ':':
        return self('CODE')
      if op == ':vi':
        self._saveCode(arg)
        self.externalEdit(cmd)
        return self('NORMAL')
      if op in ['exit', ':q']:
        self.deactivate()
        self._saveCode()
        return self('NORMAL')
      if op == ':w':
        self._saveCode(arg)
        return self('NORMAL')
    if cmd == 'CODE':
      for (i, line) in enumerate(self.getCodeLines()):
        print('%02d  |%s' % (i, line))
      codeLine = input(monoSpace(self._getCodePrompt())).strip()
      if not codeLine:
        return self('NORMAL')
      self.appendLine(codeLine)
      return self('CODE')
    if cmd == 'NORMAL':
      newCmd = input(monoSpace(self._getNormalPrompt()))
      if not newCmd:
        return self('CODE')
      c = 4
      while not self._validateNormalCommand(newCmd):
        newCmd = input(monoSpace(self._getNormalPrompt()))
        c -= 1
        if not c:
          raise KeyboardInterrupt

      if not newCmd and cmd in ['NORMAL', 'CODE']:
        return self('NORMAL' if cmd == 'CODE' else 'CODE')
      return self(newCmd)

  def __enter__(self) -> BreakPoint:
    """Activates the breakpoint"""
    return self

  def __exit__(self, exc_type, exc_value, traceback) -> None:
    """Deactivates the breakpoint"""
    if exc_type is not None:
      print(exc_type)
      print(exc_value)
