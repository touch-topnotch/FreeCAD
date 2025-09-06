# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettingsNotificationArea.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Gui_Dialog_DlgSettingsNotificationArea(object):
    def setupUi(self, Gui__Dialog__DlgSettingsNotificationArea):
        if not Gui__Dialog__DlgSettingsNotificationArea.objectName():
            Gui__Dialog__DlgSettingsNotificationArea.setObjectName(u"Gui__Dialog__DlgSettingsNotificationArea")
        Gui__Dialog__DlgSettingsNotificationArea.resize(654, 557)
        self.gridLayout_2 = QGridLayout(Gui__Dialog__DlgSettingsNotificationArea)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.NotificationAreaEnabled = QGroupBox(Gui__Dialog__DlgSettingsNotificationArea)
        self.NotificationAreaEnabled.setObjectName(u"NotificationAreaEnabled")
        self.NotificationAreaEnabled.setCheckable(True)
        self.gridLayout = QGridLayout(self.NotificationAreaEnabled)
        self.gridLayout.setObjectName(u"gridLayout")
        self.NonIntrusiveNotificationsEnabled = QGroupBox(self.NotificationAreaEnabled)
        self.NonIntrusiveNotificationsEnabled.setObjectName(u"NonIntrusiveNotificationsEnabled")
        self.NonIntrusiveNotificationsEnabled.setCheckable(True)
        self.NonIntrusiveNotificationsEnabled.setChecked(True)
        self.gridLayout_3 = QGridLayout(self.NonIntrusiveNotificationsEnabled)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.NonIntrusiveNotificationsEnabled)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.NonIntrusiveNotificationsEnabled)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.maxDuration = Gui_PrefSpinBox(self.NonIntrusiveNotificationsEnabled)
        self.maxDuration.setObjectName(u"maxDuration")
        self.maxDuration.setMinimum(0)
        self.maxDuration.setMaximum(120)
        self.maxDuration.setValue(20)
        self.maxDuration.setProperty(u"prefEntry", u"NotificationTime")
        self.maxDuration.setProperty(u"prefPath", u"NotificationArea")

        self.gridLayout_3.addWidget(self.maxDuration, 0, 1, 1, 1)

        self.minDuration = Gui_PrefSpinBox(self.NonIntrusiveNotificationsEnabled)
        self.minDuration.setObjectName(u"minDuration")
        self.minDuration.setValue(5)
        self.minDuration.setProperty(u"prefEntry", u"MinimumOnScreenTime")
        self.minDuration.setProperty(u"prefPath", u"NotificationArea")

        self.gridLayout_3.addWidget(self.minDuration, 1, 1, 1, 1)

        self.label_3 = QLabel(self.NonIntrusiveNotificationsEnabled)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.maxNotifications = Gui_PrefSpinBox(self.NonIntrusiveNotificationsEnabled)
        self.maxNotifications.setObjectName(u"maxNotifications")
        self.maxNotifications.setValue(15)
        self.maxNotifications.setProperty(u"prefEntry", u"MaxOpenNotifications")
        self.maxNotifications.setProperty(u"prefPath", u"NotificationArea")

        self.gridLayout_3.addWidget(self.maxNotifications, 2, 1, 1, 1)

        self.label_width = QLabel(self.NonIntrusiveNotificationsEnabled)
        self.label_width.setObjectName(u"label_width")

        self.gridLayout_3.addWidget(self.label_width, 3, 0, 1, 1)

        self.notificationWidth = Gui_PrefSpinBox(self.NonIntrusiveNotificationsEnabled)
        self.notificationWidth.setObjectName(u"notificationWidth")
        self.notificationWidth.setMinimum(300)
        self.notificationWidth.setMaximum(10000)
        self.notificationWidth.setValue(800)
        self.notificationWidth.setProperty(u"prefEntry", u"NotificiationWidth")
        self.notificationWidth.setProperty(u"prefPath", u"NotificationArea")

        self.gridLayout_3.addWidget(self.notificationWidth, 3, 1, 1, 1)

        self.hideNonIntrusiveNotificationsWhenWindowDeactivated = Gui_PrefCheckBox(self.NonIntrusiveNotificationsEnabled)
        self.hideNonIntrusiveNotificationsWhenWindowDeactivated.setObjectName(u"hideNonIntrusiveNotificationsWhenWindowDeactivated")
        self.hideNonIntrusiveNotificationsWhenWindowDeactivated.setChecked(True)
        self.hideNonIntrusiveNotificationsWhenWindowDeactivated.setProperty(u"prefEntry", u"HideNonIntrusiveNotificationsWhenWindowDeactivated")
        self.hideNonIntrusiveNotificationsWhenWindowDeactivated.setProperty(u"prefPath", u"NotificationArea")

        self.gridLayout_3.addWidget(self.hideNonIntrusiveNotificationsWhenWindowDeactivated, 4, 0, 1, 1)

        self.preventNonIntrusiveNotificationsWhenWindowNotActive = Gui_PrefCheckBox(self.NonIntrusiveNotificationsEnabled)
        self.preventNonIntrusiveNotificationsWhenWindowNotActive.setObjectName(u"preventNonIntrusiveNotificationsWhenWindowNotActive")
        self.preventNonIntrusiveNotificationsWhenWindowNotActive.setChecked(True)
        self.preventNonIntrusiveNotificationsWhenWindowNotActive.setProperty(u"prefEntry", u"PreventNonIntrusiveNotificationsWhenWindowNotActive")
        self.preventNonIntrusiveNotificationsWhenWindowNotActive.setProperty(u"prefPath", u"NotificationArea")

        self.gridLayout_3.addWidget(self.preventNonIntrusiveNotificationsWhenWindowNotActive, 5, 0, 1, 1)


        self.gridLayout.addWidget(self.NonIntrusiveNotificationsEnabled, 2, 0, 1, 1)

        self.GroupBoxSubscriptions = QGroupBox(self.NotificationAreaEnabled)
        self.GroupBoxSubscriptions.setObjectName(u"GroupBoxSubscriptions")
        self.gridLayout_1 = QGridLayout(self.GroupBoxSubscriptions)
        self.gridLayout_1.setObjectName(u"gridLayout_1")
        self.developerErrorSubscriptionEnabled = Gui_PrefCheckBox(self.GroupBoxSubscriptions)
        self.developerErrorSubscriptionEnabled.setObjectName(u"developerErrorSubscriptionEnabled")
        self.developerErrorSubscriptionEnabled.setChecked(False)
        self.developerErrorSubscriptionEnabled.setProperty(u"prefEntry", u"DeveloperErrorSubscriptionEnabled")
        self.developerErrorSubscriptionEnabled.setProperty(u"prefPath", u"NotificationArea")

        self.gridLayout_1.addWidget(self.developerErrorSubscriptionEnabled, 0, 0, 1, 1)

        self.developerWarningSubscriptionEnabled = Gui_PrefCheckBox(self.GroupBoxSubscriptions)
        self.developerWarningSubscriptionEnabled.setObjectName(u"developerWarningSubscriptionEnabled")
        self.developerWarningSubscriptionEnabled.setChecked(False)
        self.developerWarningSubscriptionEnabled.setProperty(u"prefEntry", u"DeveloperWarningSubscriptionEnabled")
        self.developerWarningSubscriptionEnabled.setProperty(u"prefPath", u"NotificationArea")

        self.gridLayout_1.addWidget(self.developerWarningSubscriptionEnabled, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.GroupBoxSubscriptions, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.NotificationAreaEnabled)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.maxWidgetMessages = Gui_PrefSpinBox(self.groupBox_2)
        self.maxWidgetMessages.setObjectName(u"maxWidgetMessages")
        self.maxWidgetMessages.setMaximum(10000)
        self.maxWidgetMessages.setValue(1000)
        self.maxWidgetMessages.setProperty(u"prefEntry", u"MaxWidgetMessages")
        self.maxWidgetMessages.setProperty(u"prefPath", u"NotificationArea")

        self.gridLayout_4.addWidget(self.maxWidgetMessages, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)

        self.autoRemoveUserNotifications = Gui_PrefCheckBox(self.groupBox_2)
        self.autoRemoveUserNotifications.setObjectName(u"autoRemoveUserNotifications")
        self.autoRemoveUserNotifications.setChecked(True)
        self.autoRemoveUserNotifications.setProperty(u"prefEntry", u"AutoRemoveUserNotifications")
        self.autoRemoveUserNotifications.setProperty(u"prefPath", u"NotificationArea")

        self.gridLayout_4.addWidget(self.autoRemoveUserNotifications, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.NotificationAreaEnabled, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 63, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 0, 1, 1)


        self.retranslateUi(Gui__Dialog__DlgSettingsNotificationArea)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsNotificationArea)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsNotificationArea):
        Gui__Dialog__DlgSettingsNotificationArea.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"Notification Area", None))
#if QT_CONFIG(tooltip)
        self.NotificationAreaEnabled.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"<html><head/><body><p>If checked, show the notification area in the status bar: a button with the current notification count, which can expand the detailed notification list. Optionally, with additional pop-up notifications.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.NotificationAreaEnabled.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"Enable Notification Area", None))
#if QT_CONFIG(tooltip)
        self.NonIntrusiveNotificationsEnabled.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"Enables non-intrusive pop-up notifications above the status bar notification area. Pop-up notifications can be manually dismissed by clicking on them, and also automatically dismissed by specifying a maximum and minimum duration for them to be displayed.\n"
"\n"
"Additionally, pop-up notifications can be disabled. In this case the user can still use the notification area as a quick-access location to view notifications, without the distracton of an additional pop-up.", None))
#endif // QT_CONFIG(tooltip)
        self.NonIntrusiveNotificationsEnabled.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"Enable Pop-Up Notifications", None))
        self.label_2.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"Minimum duration", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"Maximum duration", None))
#if QT_CONFIG(tooltip)
        self.maxDuration.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"<html><head/><body><p>Maximum amount of time the notification will be shown (unless mouse buttons are clicked). It also controls when user notifications will be removed if the &quot;Auto-remove user notifications&quot; setting is checked.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.maxDuration.setSuffix(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u" s", None))
#if QT_CONFIG(tooltip)
        self.minDuration.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"<html><head/><body><p>Minimum amount of time the notification will be shown (unless the notification bubble is dismissed by clicking on it).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.minDuration.setSuffix(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u" s", None))
        self.label_3.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"Maximum concurrent notification count", None))
#if QT_CONFIG(tooltip)
        self.maxNotifications.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"Maximum number of notifications that will be simultaneously present on the notification bubble.", None))
#endif // QT_CONFIG(tooltip)
        self.label_width.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"Notification bubble width", None))
#if QT_CONFIG(tooltip)
        self.notificationWidth.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"Width of the pop-up notification bubble in pixels.", None))
#endif // QT_CONFIG(tooltip)
        self.notificationWidth.setSuffix(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u" px", None))
        self.notificationWidth.setPrefix("")
#if QT_CONFIG(tooltip)
        self.hideNonIntrusiveNotificationsWhenWindowDeactivated.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"Any open pop-up notifications will disappear when another window is activated.", None))
#endif // QT_CONFIG(tooltip)
        self.hideNonIntrusiveNotificationsWhenWindowDeactivated.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"Hide when other window is activated", None))
#if QT_CONFIG(tooltip)
        self.preventNonIntrusiveNotificationsWhenWindowNotActive.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"Prevent pop-up notifications from appearing when the FreeCAD window is not the active window.", None))
#endif // QT_CONFIG(tooltip)
        self.preventNonIntrusiveNotificationsWhenWindowNotActive.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"Do not show when window is inactive", None))
#if QT_CONFIG(tooltip)
        self.GroupBoxSubscriptions.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"Additional notification sources to show in the notification area.", None))
#endif // QT_CONFIG(tooltip)
        self.GroupBoxSubscriptions.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"Additional Data Sources", None))
#if QT_CONFIG(tooltip)
        self.developerErrorSubscriptionEnabled.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"Errors intended for developers will appear in the notification area.", None))
#endif // QT_CONFIG(tooltip)
        self.developerErrorSubscriptionEnabled.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"Debug errors", None))
#if QT_CONFIG(tooltip)
        self.developerWarningSubscriptionEnabled.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"Warnings intended for developers will appear in the notification area.", None))
#endif // QT_CONFIG(tooltip)
        self.developerWarningSubscriptionEnabled.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"Debug warnings", None))
#if QT_CONFIG(tooltip)
        self.groupBox_2.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"Controls the amount of notifications to show in the list.", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"Notifications List", None))
#if QT_CONFIG(tooltip)
        self.maxWidgetMessages.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"Limits the number of notifications that will be kept in the list. If 0, there is no limit.", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"Maximum notification count", None))
#if QT_CONFIG(tooltip)
        self.autoRemoveUserNotifications.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"Removes the user notifications from the notifications list after the maximum duration for pop-up notifications has lapsed.", None))
#endif // QT_CONFIG(tooltip)
        self.autoRemoveUserNotifications.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsNotificationArea", u"Auto-remove user notifications", None))
    # retranslateUi

