import subprocess

CMD = '''
on run argv
  display notification (item 2 of argv) with title (item 1 of argv)
end run
'''


def desktop_popup(title, text):
    subprocess.call(['osascript', '-e', CMD, title, text])
    subprocess.call(['afplay', '/System/Library/Sounds/Hero.aiff'])


if __name__ == "__main__":
    desktop_popup("Test Title", "Test alert text here")
