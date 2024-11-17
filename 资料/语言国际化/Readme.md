
0、安装依赖组件（只需安装一次）这是旧版本，新版本读取不了xlsx
sudo pip install xlrd==1.2.0

1.运行脚本：
python localized.py excel.xlsx

注：
localized.py 为脚本文件
excel.xlsx 为 excel表路径，按实际修改

https://blog.csdn.net/Deathless_Dawn/article/details/120511981
可以先使用 selenium 自动从网站下载腾讯文档
/**
     * 由于腾讯文档 CSS 节点经常变动，仅需要更新下方几个 CSS 选择器节点即可
     *
     * STEP_1 - STEP_4 为下载文档操作的四步点击操作对应的节点
     */
    private const val CSS_CHECK_LOGIN = "self-info"
    private const val CSS_STEP_1 = "#main-menu-file"
    private const val CSS_STEP_2 = ".mainmenu-submenu-exportAs"
    private const val CSS_STEP_3 = ".mainmenu-item-export-local"
    private const val CSS_STEP_4 = "button.dui-button:nth-child(2)"
