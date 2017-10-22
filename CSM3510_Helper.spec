# -*- mode: python -*-

block_cipher = None


a = Analysis(['CSM3510_Helper.py'],
             pathex=['C:\\Python\\Python35-32\\Lib\\site-packages\\PyQt5\\Qt\\bin', 'C:\\Users\\admin\\Documents\\junglefive\\github\\SerialPortTools\\CSM3510_Helper'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='CSM3510_Helper',
          debug=False,
          strip=False,
          upx=True,
          console=True )
