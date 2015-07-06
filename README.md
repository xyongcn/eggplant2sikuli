# eggplant2sikuli
a converter from eggplant to sikuli

## 使用方法
ets.py C:\\Users\\Administrator\\Documents\\test.suite D:\\share  
第一个参数是eggplant测试suite的文件夹路径，这里以C:\\Users\\Administrator\\Documents\\test.suite为例，第二个参数是欲生成的sikuli文件夹的父目录，这里以D:\\share为例

## 处理过程
1. 在D:\\share下以suite的名字新建一个目录test.sikuli 
2. 把suite中Images文件夹的图片都拷贝到test.sikuli中
3. 对Scripts中的脚本（按照sikuli的要求，只能有一个脚本）进行处理，转换后的脚本生成到test.sikuli文件夹下，名字设定为test.py（必须于文件夹名字相同）

## 转换过程
1. 在sikuli脚本的第一行写入import shutil
2. 扫描eggplant脚本中的每一行，按照事先设定好的字典进行转换，如Click转换为click，WaitFor转换为wait，Return转换为Key.ENTER，目前这个字典还有待进一步的扩充。
3. 再按照sikuli的语法写入到新脚本中，例如函数以name(arg1,arg2)的形式调用，图片名后应加入.png后缀。

## Example
test.suite文件夹是eggplant文件夹，运行脚本之后生成的sikuli文件夹应该与test.sikuli文件夹相同

### eggplant脚本
完成了打开firefox，进入百度，然后搜索sikuli，最后关闭浏览器的操作

    DoubleClick "image0001"
    Click "image0002"
    WaitFor 10,"MozillaFirefox"
    TypeText "www.baidu.com",Return
    WaitFor 10,"image0004"
    TypeText "sikuli",Return
    Click "image0003"

### 转换后的sikuli脚本
    import shutil
    doubleClick("image0001.png")
    click("image0002.png")
    wait("MozillaFirefox.png",10)
    type("www.baidu.com")
    type(Key.ENTER)
    wait("image0004.png",10)
    type("sikuli")
    type(Key.ENTER)
    click("image0003.png")

# ldtpeditor2sikuli
a converter from ldtpeditor to sikuli

## 使用方法
ldtpeditorts.py D:\\gcalc.py D:\\share\\gcalc.py  
第一个参数是ldtpeditor脚本路径，第二个参数是欲生成的sikuli脚本的路径

## 转换过程
1. 在sikuli脚本的第一行写入import shutil
2. 扫描ldtpeditor脚本中的每一行，按照事先设定好的字典进行转换，如click仍对应click，waittillguiexist对应wait(pic,FOREVER)
3. 按照sikuli的语法写入到新脚本中，如图片名后应加入.png后缀，同时要以双引号引起来等。

## Example
录制了gedit的新建文档和打开文档操作

### ldtpeditor脚本
    from ldtp import *
	from ldtputils import *
	
	try:
		wait (3)
		click ("*gedit*", "btnNew")
		wait (2)
		click ("*gedit*", "btnOpen")
		waittillguiexist ("dlgOpenFiles")
		click ("dlgOpenFiles", "tbtnroot")
		wait (5)
		click ("dlgOpenFiles", "btnCancel")
		waittillguinotexist ("dlgOpenFiles")
	except LdtpExecutionError, msg:
		raise

### 转换后的sikuli脚本
	import shutil
	wait (3)
	click("*gedit*-btnNew.png")
	wait (2)
	click("*gedit*-btnOpen.png")
	wait("dlgOpenFiles.png",FOREVER)
	click("dlgOpenFiles-tbtnroot.png")
	wait (5)
	click("dlgOpenFiles-btnCancel.png")
	waitVanish("dlgOpenFiles.png",FOREVER)