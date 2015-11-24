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
    
# systemtap2sikuli
a converter from systemtap to sikuli

## 使用方法
stapts.py D:\\calculator-test-full D:\\share\\calculator.py
第一个参数是systemtap脚本的输出文件，第二个参数是欲生成的sikuli文件的路径

## 转换过程
1. 扫描输入中的每一行，按照事先设定好的字典进行转换，如gtk_button_clicked转换为click等，目前这个字典还有待进一步的扩充。
2. 再按照sikuli的语法写入到新脚本中，例如函数以name(arg1,arg2)的形式调用，图片名后应加入.png后缀等。

## Example
录制了计算器的一些操作

### calculator-test-full输出文件

    1440055154 : 7339 : gnome-calculato : gtk_button_clicked : 9
	1440055155 : 7339 : gnome-calculato : gtk_button_clicked : ×
	1440055156 : 7339 : gnome-calculato : gtk_button_clicked : (
	1440055157 : 7339 : gnome-calculato : gtk_button_clicked : 3
	1440055158 : 7339 : gnome-calculato : gtk_button_clicked : .
	1440055159 : 7339 : gnome-calculato : gtk_button_clicked : 2
	1440055160 : 7339 : gnome-calculato : gtk_button_clicked : +
	1440055161 : 7339 : gnome-calculato : gtk_button_clicked : 0
	1440055162 : 7339 : gnome-calculato : gtk_button_clicked : .
	1440055162 : 7339 : gnome-calculato : gtk_button_clicked : 8
	1440055164 : 7339 : gnome-calculato : gtk_button_clicked : )
	1440055167 : 7339 : gnome-calculato : gtk_button_clicked : −
	1440055167 : 7339 : gnome-calculato : gtk_button_clicked : 3
	1440055168 : 7339 : gnome-calculato : gtk_button_clicked : 0
	1440055169 : 7339 : gnome-calculato : gtk_button_clicked : =
	1440055170 : 7339 : gnome-calculato : math_equation_clear : self=0xa2a290
	1440055173 : 7339 : gnome-calculato : gtk_button_clicked : 4
	1440055174 : 7339 : gnome-calculato : math_equation_insert_square : self=0xa2a290
	1440055175 : 7339 : gnome-calculato : gtk_button_clicked : +
	1440055177 : 7339 : gnome-calculato : gtk_button_clicked : √
	1440055177 : 7339 : gnome-calculato : gtk_button_clicked : 9
	1440055181 : 7339 : gnome-calculato : gtk_button_clicked : =
	1440055187 : 7339 : gnome-calculato : math_equation_clear : self=0xa2a290
	1440055227 : 7339 : gnome-calculato : gtk_button_clicked : 1
	1440055227 : 7339 : gnome-calculato : gtk_button_clicked : 0
	1440055229 : 7339 : gnome-calculato : gtk_button_clicked : +
	1440055231 : 7339 : gnome-calculato : gtk_button_clicked : 8
	1440055232 : 7339 : gnome-calculato : gtk_button_clicked : %
	1440055232 : 7339 : gnome-calculato : gtk_button_clicked : =
	1440055272 : 7339 : gnome-calculato : gtk_button_clicked : 9
	1440055276 : 7339 : gnome-calculato : math_equation_insert_square : self=0xa2a290
	1440055281 : 7339 : gnome-calculato : gtk_button_clicked : −
	1440055282 : 7339 : gnome-calculato : gtk_button_clicked : 3
	1440055283 : 7339 : gnome-calculato : gtk_button_clicked : =
	1440055284 : 7339 : gnome-calculato : math_equation_undo : self=0xa2a290
	1440055288 : 7339 : gnome-calculato : gtk_button_clicked : .
	1440055288 : 7339 : gnome-calculato : gtk_button_clicked : 2
	1440055289 : 7339 : gnome-calculato : gtk_button_clicked : =
	1440055291 : 7339 : gnome-calculato : math_equation_clear : self=0xa2a290

### 转换后的sikuli脚本
    click("frmCalculator-btnNumeric9.png")
	click("frmCalculator-btnNumeric9.png")
	click("math_equation_insert_subtract.png")
	click("frmCalculator-btnNumeric3.png")
	click("frmCalculator-btnNumeric3.png")
	click("math_equation_solve.png")
	click("math_equation_clear.png")
	click("math_equation_clear.png")
	click("frmCalculator-btnNumeric8.png")
	click("math_equation_insert_square.png")
	click("math_equation_solve.png")
	click("math_equation_undo.png")
	click("math_equation_insert_subtract.png")
	click("frmCalculator-btnNumeric3.png")
	click("math_equation_solve.png")
	click("math_equation_clear.png")
	click("frmCalculator-btnNumeric9.png")
	click("math_equation_insert_numeric_point.png")
	click("frmCalculator-btnNumeric2.png")
	click("math_equation_insert_subtract.png")
	click("frmCalculator-btnNumeric3.png")
	click("math_equation_insert_numeric_point.png")
	click("frmCalculator-btnNumeric1.png")
	click("math_equation_solve.png")
	click("math_equation_clear.png")
