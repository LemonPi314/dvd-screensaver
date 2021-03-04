# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['dvd-screensaver.py'],
             pathex=['C:\\Users\\Timothy Pavlushik\\Documents\\Visual Studio Code\\Projects\\dvd-screensaver'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas += [('dvd-screensaver/images/1/normal/dvd-logo-1-blue.png', 'C:\\Users\\Timothy Pavlushik\\Documents\\Visual Studio Code\\Projects\\dvd-screensaver\\images\\1\\normal\\dvd-logo-1-blue.png', 'DATA'),
('dvd-screensaver/images/1/normal/dvd-logo-1-cyan.png', 'C:\\Users\\Timothy Pavlushik\\Documents\\Visual Studio Code\\Projects\\dvd-screensaver\\images\\1\\normal\\dvd-logo-1-cyan.png', 'DATA'),
('dvd-screensaver/images/1/normal/dvd-logo-1-green.png', 'C:\\Users\\Timothy Pavlushik\\Documents\\Visual Studio Code\\Projects\\dvd-screensaver\\images\\1\\normal\\dvd-logo-1-green.png', 'DATA'),
('dvd-screensaver/images/1/normal/dvd-logo-1-magenta.png', 'C:\\Users\\Timothy Pavlushik\\Documents\\Visual Studio Code\\Projects\\dvd-screensaver\\images\\1\\normal\\dvd-logo-1-magenta.png', 'DATA'),
('dvd-screensaver/images/1/normal/dvd-logo-1-orange.png', 'C:\\Users\\Timothy Pavlushik\\Documents\\Visual Studio Code\\Projects\\dvd-screensaver\\images\\1\\normal\\dvd-logo-1-orange.png', 'DATA'),
('dvd-screensaver/images/1/normal/dvd-logo-1-purple.png', 'C:\\Users\\Timothy Pavlushik\\Documents\\Visual Studio Code\\Projects\\dvd-screensaver\\images\\1\\normal\\dvd-logo-1-purple.png', 'DATA'),
('dvd-screensaver/images/1/normal/dvd-logo-1-red.png', 'C:\\Users\\Timothy Pavlushik\\Documents\\Visual Studio Code\\Projects\\dvd-screensaver\\images\\1\\normal\\dvd-logo-1-red.png', 'DATA'),
('dvd-screensaver/images/1/normal/dvd-logo-1-yellow.png', 'C:\\Users\\Timothy Pavlushik\\Documents\\Visual Studio Code\\Projects\\dvd-screensaver\\images\\1\\normal\\dvd-logo-1-yellow.png', 'DATA'),
('dvd-screensaver/images/current-image/current-image.png', 'C:\\Users\\Timothy Pavlushik\\Documents\\Visual Studio Code\\Projects\\dvd-screensaver\\images\\current-image\\current-image.png', 'DATA')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='dvd-screensaver',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )

#coll = COLLECT(exe,
#               a.binaries,
#               a.zipfiles,
#               a.datas,
#               strip=False,
#               upx=True,
#               name='dvd-screensaver')