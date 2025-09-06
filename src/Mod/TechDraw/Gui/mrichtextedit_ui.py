# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mrichtextedit.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QSizePolicy, QSpacerItem, QTextEdit, QToolButton,
    QVBoxLayout, QWidget)

from mtextedit import MTextEdit
import TechDraw_rc
import TechDraw_rc

class Ui_MRichTextEdit(object):
    def setupUi(self, MRichTextEdit):
        if not MRichTextEdit.objectName():
            MRichTextEdit.setObjectName(u"MRichTextEdit")
        MRichTextEdit.resize(879, 312)
        MRichTextEdit.setWindowTitle(u"")
        self.verticalLayout = QVBoxLayout(MRichTextEdit)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.f_toolbar = QWidget(MRichTextEdit)
        self.f_toolbar.setObjectName(u"f_toolbar")
        self.horizontalLayout = QHBoxLayout(self.f_toolbar)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.f_save = QToolButton(self.f_toolbar)
        self.f_save.setObjectName(u"f_save")
        icon = QIcon()
        icon.addFile(u":/icons/MRTE/document-save.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.f_save.setIcon(icon)

        self.horizontalLayout.addWidget(self.f_save)

        self.f_exit = QToolButton(self.f_toolbar)
        self.f_exit.setObjectName(u"f_exit")
        icon1 = QIcon()
        icon1.addFile(u":/icons/MRTE/application-exit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.f_exit.setIcon(icon1)

        self.horizontalLayout.addWidget(self.f_exit)

        self.line_7 = QFrame(self.f_toolbar)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_7)

        self.f_paragraph = QComboBox(self.f_toolbar)
        self.f_paragraph.setObjectName(u"f_paragraph")
        self.f_paragraph.setFocusPolicy(Qt.ClickFocus)
        self.f_paragraph.setEditable(True)

        self.horizontalLayout.addWidget(self.f_paragraph)

        self.line_4 = QFrame(self.f_toolbar)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_4)

        self.f_undo = QToolButton(self.f_toolbar)
        self.f_undo.setObjectName(u"f_undo")
        self.f_undo.setEnabled(False)
        self.f_undo.setFocusPolicy(Qt.ClickFocus)
        icon2 = QIcon()
        icon2.addFile(u":/icons/MRTE/edit-undo.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.f_undo.setIcon(icon2)
        self.f_undo.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.f_undo)

        self.f_redo = QToolButton(self.f_toolbar)
        self.f_redo.setObjectName(u"f_redo")
        self.f_redo.setEnabled(False)
        self.f_redo.setFocusPolicy(Qt.ClickFocus)
        icon3 = QIcon()
        icon3.addFile(u":/icons/MRTE/edit-redo.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.f_redo.setIcon(icon3)
        self.f_redo.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.f_redo)

        self.f_cut = QToolButton(self.f_toolbar)
        self.f_cut.setObjectName(u"f_cut")
        self.f_cut.setFocusPolicy(Qt.ClickFocus)
        icon4 = QIcon()
        icon4.addFile(u":/icons/MRTE/edit-cut.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.f_cut.setIcon(icon4)
        self.f_cut.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.f_cut)

        self.f_copy = QToolButton(self.f_toolbar)
        self.f_copy.setObjectName(u"f_copy")
        self.f_copy.setFocusPolicy(Qt.ClickFocus)
        icon5 = QIcon()
        icon5.addFile(u":/icons/MRTE/edit-copy.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.f_copy.setIcon(icon5)
        self.f_copy.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.f_copy)

        self.f_paste = QToolButton(self.f_toolbar)
        self.f_paste.setObjectName(u"f_paste")
        self.f_paste.setFocusPolicy(Qt.ClickFocus)
        icon6 = QIcon()
        icon6.addFile(u":/icons/MRTE/edit-paste.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.f_paste.setIcon(icon6)
        self.f_paste.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.f_paste)

        self.line = QFrame(self.f_toolbar)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.f_link = QToolButton(self.f_toolbar)
        self.f_link.setObjectName(u"f_link")
        self.f_link.setFocusPolicy(Qt.ClickFocus)
        icon7 = QIcon()
        icon7.addFile(u":/icons/MRTE/internet-web-browser.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.f_link.setIcon(icon7)
        self.f_link.setIconSize(QSize(16, 16))
        self.f_link.setCheckable(True)

        self.horizontalLayout.addWidget(self.f_link)

        self.line_3 = QFrame(self.f_toolbar)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.f_bold = QToolButton(self.f_toolbar)
        self.f_bold.setObjectName(u"f_bold")
        self.f_bold.setFocusPolicy(Qt.ClickFocus)
#if QT_CONFIG(tooltip)
        self.f_bold.setToolTip(u"Bold (Ctrl+B)")
#endif // QT_CONFIG(tooltip)
        icon8 = QIcon()
        icon8.addFile(u":/icons/MRTE/textBold.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.f_bold.setIcon(icon8)
        self.f_bold.setIconSize(QSize(16, 16))
        self.f_bold.setCheckable(True)

        self.horizontalLayout.addWidget(self.f_bold)

        self.f_italic = QToolButton(self.f_toolbar)
        self.f_italic.setObjectName(u"f_italic")
        self.f_italic.setFocusPolicy(Qt.ClickFocus)
        icon9 = QIcon()
        icon9.addFile(u":/icons/MRTE/textItalic.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.f_italic.setIcon(icon9)
        self.f_italic.setIconSize(QSize(16, 16))
        self.f_italic.setCheckable(True)

        self.horizontalLayout.addWidget(self.f_italic)

        self.f_underline = QToolButton(self.f_toolbar)
        self.f_underline.setObjectName(u"f_underline")
        self.f_underline.setFocusPolicy(Qt.ClickFocus)
        icon10 = QIcon()
        icon10.addFile(u":/icons/MRTE/textUnderline.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.f_underline.setIcon(icon10)
        self.f_underline.setIconSize(QSize(16, 16))
        self.f_underline.setCheckable(True)

        self.horizontalLayout.addWidget(self.f_underline)

        self.f_strikeout = QToolButton(self.f_toolbar)
        self.f_strikeout.setObjectName(u"f_strikeout")
        icon11 = QIcon()
        icon11.addFile(u":/icons/MRTE/textStrike.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.f_strikeout.setIcon(icon11)
        self.f_strikeout.setIconSize(QSize(16, 16))
        self.f_strikeout.setCheckable(True)

        self.horizontalLayout.addWidget(self.f_strikeout)

        self.line_5 = QFrame(self.f_toolbar)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_5)

        self.f_list_bullet = QToolButton(self.f_toolbar)
        self.f_list_bullet.setObjectName(u"f_list_bullet")
        self.f_list_bullet.setFocusPolicy(Qt.ClickFocus)
        icon12 = QIcon()
        icon12.addFile(u":/icons/MRTE/listBullet.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.f_list_bullet.setIcon(icon12)
        self.f_list_bullet.setIconSize(QSize(16, 16))
        self.f_list_bullet.setCheckable(True)

        self.horizontalLayout.addWidget(self.f_list_bullet)

        self.f_list_ordered = QToolButton(self.f_toolbar)
        self.f_list_ordered.setObjectName(u"f_list_ordered")
        self.f_list_ordered.setFocusPolicy(Qt.ClickFocus)
        icon13 = QIcon()
        icon13.addFile(u":/icons/MRTE/listNumber.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.f_list_ordered.setIcon(icon13)
        self.f_list_ordered.setIconSize(QSize(16, 16))
        self.f_list_ordered.setCheckable(True)

        self.horizontalLayout.addWidget(self.f_list_ordered)

        self.f_indent_dec = QToolButton(self.f_toolbar)
        self.f_indent_dec.setObjectName(u"f_indent_dec")
        self.f_indent_dec.setFocusPolicy(Qt.ClickFocus)
        icon14 = QIcon()
        icon14.addFile(u":/icons/MRTE/indentLess.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.f_indent_dec.setIcon(icon14)
        self.f_indent_dec.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.f_indent_dec)

        self.f_indent_inc = QToolButton(self.f_toolbar)
        self.f_indent_inc.setObjectName(u"f_indent_inc")
        self.f_indent_inc.setFocusPolicy(Qt.ClickFocus)
        icon15 = QIcon()
        icon15.addFile(u":/icons/MRTE/indentMore.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.f_indent_inc.setIcon(icon15)
        self.f_indent_inc.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.f_indent_inc)

        self.line_2 = QFrame(self.f_toolbar)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.f_fgcolor = QToolButton(self.f_toolbar)
        self.f_fgcolor.setObjectName(u"f_fgcolor")
        self.f_fgcolor.setMinimumSize(QSize(0, 0))
        self.f_fgcolor.setFocusPolicy(Qt.ClickFocus)
        icon16 = QIcon()
        icon16.addFile(u":/icons/MRTE/fgColor.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.f_fgcolor.setIcon(icon16)
        self.f_fgcolor.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.f_fgcolor)

        self.f_bgcolor = QToolButton(self.f_toolbar)
        self.f_bgcolor.setObjectName(u"f_bgcolor")
        self.f_bgcolor.setFocusPolicy(Qt.ClickFocus)
        icon17 = QIcon()
        icon17.addFile(u":/icons/MRTE/bgColor.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.f_bgcolor.setIcon(icon17)
        self.f_bgcolor.setIconSize(QSize(16, 16))
        self.f_bgcolor.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.f_bgcolor.setArrowType(Qt.NoArrow)

        self.horizontalLayout.addWidget(self.f_bgcolor)

        self.f_fontsize = QComboBox(self.f_toolbar)
        self.f_fontsize.setObjectName(u"f_fontsize")
        self.f_fontsize.setFocusPolicy(Qt.ClickFocus)
        self.f_fontsize.setEditable(True)

        self.horizontalLayout.addWidget(self.f_fontsize)

        self.line_6 = QFrame(self.f_toolbar)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_6)

        self.f_image = QToolButton(self.f_toolbar)
        self.f_image.setObjectName(u"f_image")
        self.f_image.setText(u"")
        icon18 = QIcon()
        icon18.addFile(u":/icons/MRTE/insertImage.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.f_image.setIcon(icon18)

        self.horizontalLayout.addWidget(self.f_image)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.f_menu = QToolButton(self.f_toolbar)
        self.f_menu.setObjectName(u"f_menu")
        icon19 = QIcon()
        icon19.addFile(u":/icons/MRTE/menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.f_menu.setIcon(icon19)

        self.horizontalLayout.addWidget(self.f_menu)

        self.f_paragraph.raise_()
        self.line_4.raise_()
        self.f_undo.raise_()
        self.f_redo.raise_()
        self.f_cut.raise_()
        self.f_copy.raise_()
        self.f_paste.raise_()
        self.line.raise_()
        self.f_link.raise_()
        self.line_3.raise_()
        self.f_italic.raise_()
        self.f_underline.raise_()
        self.line_2.raise_()
        self.f_fontsize.raise_()
        self.line_5.raise_()
        self.f_list_bullet.raise_()
        self.f_list_ordered.raise_()
        self.f_indent_dec.raise_()
        self.f_indent_inc.raise_()
        self.f_bold.raise_()
        self.f_bgcolor.raise_()
        self.f_strikeout.raise_()
        self.f_image.raise_()
        self.line_6.raise_()
        self.f_menu.raise_()
        self.f_fgcolor.raise_()
        self.f_save.raise_()
        self.f_exit.raise_()
        self.line_7.raise_()

        self.verticalLayout.addWidget(self.f_toolbar)

        self.f_textedit = MTextEdit(MRichTextEdit)
        self.f_textedit.setObjectName(u"f_textedit")
        self.f_textedit.setAutoFormatting(QTextEdit.AutoNone)
        self.f_textedit.setTabChangesFocus(True)

        self.verticalLayout.addWidget(self.f_textedit)

        QWidget.setTabOrder(self.f_textedit, self.f_strikeout)
        QWidget.setTabOrder(self.f_strikeout, self.f_image)
        QWidget.setTabOrder(self.f_image, self.f_menu)

        self.retranslateUi(MRichTextEdit)

        QMetaObject.connectSlotsByName(MRichTextEdit)
    # setupUi

    def retranslateUi(self, MRichTextEdit):
#if QT_CONFIG(tooltip)
        self.f_save.setToolTip(QCoreApplication.translate("MRichTextEdit", u"Save changes", None))
#endif // QT_CONFIG(tooltip)
        self.f_save.setText("")
#if QT_CONFIG(tooltip)
        self.f_exit.setToolTip(QCoreApplication.translate("MRichTextEdit", u"Close editor", None))
#endif // QT_CONFIG(tooltip)
        self.f_exit.setText("")
#if QT_CONFIG(tooltip)
        self.f_paragraph.setToolTip(QCoreApplication.translate("MRichTextEdit", u"Paragraph formatting", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.f_undo.setToolTip(QCoreApplication.translate("MRichTextEdit", u"Undo (Ctrl+Z)", None))
#endif // QT_CONFIG(tooltip)
        self.f_undo.setText(QCoreApplication.translate("MRichTextEdit", u"Undo", None))
#if QT_CONFIG(tooltip)
        self.f_redo.setToolTip(QCoreApplication.translate("MRichTextEdit", u"Redo", None))
#endif // QT_CONFIG(tooltip)
        self.f_redo.setText(QCoreApplication.translate("MRichTextEdit", u"Redo", None))
#if QT_CONFIG(tooltip)
        self.f_cut.setToolTip(QCoreApplication.translate("MRichTextEdit", u"Cut (Ctrl+X)", None))
#endif // QT_CONFIG(tooltip)
        self.f_cut.setText(QCoreApplication.translate("MRichTextEdit", u"Cut", None))
#if QT_CONFIG(tooltip)
        self.f_copy.setToolTip(QCoreApplication.translate("MRichTextEdit", u"Copy (Ctrl+C)", None))
#endif // QT_CONFIG(tooltip)
        self.f_copy.setText(QCoreApplication.translate("MRichTextEdit", u"Copy", None))
#if QT_CONFIG(tooltip)
        self.f_paste.setToolTip(QCoreApplication.translate("MRichTextEdit", u"Paste (Ctrl+V)", None))
#endif // QT_CONFIG(tooltip)
        self.f_paste.setText(QCoreApplication.translate("MRichTextEdit", u"Paste", None))
#if QT_CONFIG(tooltip)
        self.f_link.setToolTip(QCoreApplication.translate("MRichTextEdit", u"Link (Ctrl+L)", None))
#endif // QT_CONFIG(tooltip)
        self.f_link.setText(QCoreApplication.translate("MRichTextEdit", u"Link", None))
        self.f_bold.setText(QCoreApplication.translate("MRichTextEdit", u"Bold", None))
#if QT_CONFIG(tooltip)
        self.f_italic.setToolTip(QCoreApplication.translate("MRichTextEdit", u"Italic (Ctrl+I)", None))
#endif // QT_CONFIG(tooltip)
        self.f_italic.setText(QCoreApplication.translate("MRichTextEdit", u"Italic", None))
#if QT_CONFIG(tooltip)
        self.f_underline.setToolTip(QCoreApplication.translate("MRichTextEdit", u"Underline (Ctrl+U)", None))
#endif // QT_CONFIG(tooltip)
        self.f_underline.setText(QCoreApplication.translate("MRichTextEdit", u"Underline", None))
#if QT_CONFIG(tooltip)
        self.f_strikeout.setToolTip(QCoreApplication.translate("MRichTextEdit", u"Strikethrough text", None))
#endif // QT_CONFIG(tooltip)
        self.f_strikeout.setText(QCoreApplication.translate("MRichTextEdit", u"Strikethrough", None))
#if QT_CONFIG(tooltip)
        self.f_list_bullet.setToolTip(QCoreApplication.translate("MRichTextEdit", u"Bullet list (Ctrl+-)", None))
#endif // QT_CONFIG(tooltip)
        self.f_list_bullet.setText("")
#if QT_CONFIG(tooltip)
        self.f_list_ordered.setToolTip(QCoreApplication.translate("MRichTextEdit", u"Ordered list (Ctrl+=)", None))
#endif // QT_CONFIG(tooltip)
        self.f_list_ordered.setText("")
#if QT_CONFIG(tooltip)
        self.f_indent_dec.setToolTip(QCoreApplication.translate("MRichTextEdit", u"Decrease indentation (Ctrl+,)", None))
#endif // QT_CONFIG(tooltip)
        self.f_indent_dec.setText(QCoreApplication.translate("MRichTextEdit", u"Decrease Indentation", None))
#if QT_CONFIG(tooltip)
        self.f_indent_inc.setToolTip(QCoreApplication.translate("MRichTextEdit", u"Increase indentation (Ctrl+.)", None))
#endif // QT_CONFIG(tooltip)
        self.f_indent_inc.setText(QCoreApplication.translate("MRichTextEdit", u"Increase Indentation", None))
#if QT_CONFIG(tooltip)
        self.f_fgcolor.setToolTip(QCoreApplication.translate("MRichTextEdit", u"Text foreground color", None))
#endif // QT_CONFIG(tooltip)
        self.f_fgcolor.setText("")
#if QT_CONFIG(tooltip)
        self.f_bgcolor.setToolTip(QCoreApplication.translate("MRichTextEdit", u"Text background color", None))
#endif // QT_CONFIG(tooltip)
        self.f_bgcolor.setText(QCoreApplication.translate("MRichTextEdit", u"Background", None))
#if QT_CONFIG(tooltip)
        self.f_fontsize.setToolTip(QCoreApplication.translate("MRichTextEdit", u"Font size", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.f_menu.setToolTip(QCoreApplication.translate("MRichTextEdit", u"More functions", None))
#endif // QT_CONFIG(tooltip)
        self.f_menu.setText("")
#if QT_CONFIG(tooltip)
        self.f_textedit.setToolTip(QCoreApplication.translate("MRichTextEdit", u"More functions", None))
#endif // QT_CONFIG(tooltip)
        pass
    # retranslateUi

