/***************************************************************************
 *   Copyright (c) 2012 Werner Mayer <wmayer[at]users.sourceforge.net>     *
 *                                                                         *
 *   This file is part of the FreeCAD CAx development system.              *
 *                                                                         *
 *   This library is free software; you can redistribute it and/or         *
 *   modify it under the terms of the GNU Library General Public           *
 *   License as published by the Free Software Foundation; either          *
 *   version 2 of the License, or (at your option) any later version.      *
 *                                                                         *
 *   This library  is distributed in the hope that it will be useful,      *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU Library General Public License for more details.                  *
 *                                                                         *
 *   You should have received a copy of the GNU Library General Public     *
 *   License along with this library; see the file COPYING.LIB. If not,    *
 *   write to the Free Software Foundation, Inc., 59 Temple Place,         *
 *   Suite 330, Boston, MA  02111-1307, USA                                *
 *                                                                         *
 ***************************************************************************/

#include "PreCompiled.h"

#ifndef _PreComp_
# include <limits>
# include <QMessageBox>
#endif

#include <App/Application.h>
#include <App/Document.h>
#include <App/DocumentObject.h>
#include <Gui/Application.h>
#include <Gui/BitmapFactory.h>
#include <Gui/CommandT.h>
#include <Gui/Document.h>
#include <Gui/ViewProvider.h>
#include <Mod/Part/App/FeatureOffset.h>

#include "TaskOffset.h"
#include "ui_TaskOffset.h"


using namespace PartGui;

class OffsetWidget::Private
{
public:
    Ui_TaskOffset ui{};
    Part::Offset* offset{nullptr};
};

/* TRANSLATOR PartGui::OffsetWidget */

OffsetWidget::OffsetWidget(Part::Offset* offset, QWidget* parent)
  : d(new Private())
{
    Q_UNUSED(parent);
    Gui::Command::runCommand(Gui::Command::App, "from FreeCAD import Base");
    Gui::Command::runCommand(Gui::Command::App, "import Part");

    d->offset = offset;
    d->ui.setupUi(this);
    setupConnections();

    d->ui.spinOffset->setUnit(Base::Unit::Length);
    d->ui.spinOffset->setRange(-std::numeric_limits<int>::max(),
                                std::numeric_limits<int>::max());
    d->ui.spinOffset->setSingleStep(0.1);
    d->ui.facesButton->hide();

    bool is_2d = d->offset->isDerivedFrom<Part::Offset2D>();
    d->ui.selfIntersection->setVisible(!is_2d);
    if(is_2d)
        d->ui.modeType->removeItem(2);//remove Recto-Verso mode, not supported by 2d offset

    //block signals to fill values read out from feature...
    bool block = true;
    d->ui.fillOffset->blockSignals(block);
    d->ui.intersection->blockSignals(block);
    d->ui.selfIntersection->blockSignals(block);
    d->ui.modeType->blockSignals(block);
    d->ui.joinType->blockSignals(block);
    d->ui.spinOffset->blockSignals(block);

    //read values from feature
    d->ui.spinOffset->setValue(d->offset->Value.getValue());
    d->ui.fillOffset->setChecked(offset->Fill.getValue());
    d->ui.intersection->setChecked(offset->Intersection.getValue());
    d->ui.selfIntersection->setChecked(offset->SelfIntersection.getValue());
    long mode = offset->Mode.getValue();
    if (mode >= 0 && mode < d->ui.modeType->count())
        d->ui.modeType->setCurrentIndex(mode);
    long join = offset->Join.getValue();
    if (join >= 0 && join < d->ui.joinType->count())
        d->ui.joinType->setCurrentIndex(join);

    //unblock signals
    block = false;
    d->ui.fillOffset->blockSignals(block);
    d->ui.intersection->blockSignals(block);
    d->ui.selfIntersection->blockSignals(block);
    d->ui.modeType->blockSignals(block);
    d->ui.joinType->blockSignals(block);
    d->ui.spinOffset->blockSignals(block);

    d->ui.spinOffset->bind(d->offset->Value);
}

OffsetWidget::~OffsetWidget()
{
    delete d;
}

void OffsetWidget::setupConnections()
{
    // clang-format off
    connect(d->ui.spinOffset, qOverload<double>(&Gui::QuantitySpinBox::valueChanged),
            this, &OffsetWidget::onSpinOffsetValueChanged);
    connect(d->ui.modeType, qOverload<int>(&QComboBox::activated),
            this, &OffsetWidget::onModeTypeActivated);
    connect(d->ui.joinType, qOverload<int>(&QComboBox::activated),
            this, &OffsetWidget::onJoinTypeActivated);
    connect(d->ui.intersection, &QCheckBox::toggled,
            this, &OffsetWidget::onIntersectionToggled);
    connect(d->ui.selfIntersection, &QCheckBox::toggled,
            this, &OffsetWidget::onSelfIntersectionToggled);
    connect(d->ui.fillOffset, &QCheckBox::toggled,
            this, &OffsetWidget::onFillOffsetToggled);
    connect(d->ui.updateView, &QCheckBox::toggled,
            this, &OffsetWidget::onUpdateViewToggled);
    // clang-format on
}

Part::Offset* OffsetWidget::getObject() const
{
    return d->offset;
}

void OffsetWidget::onSpinOffsetValueChanged(double val)
{
    d->offset->Value.setValue(val);
    if (d->ui.updateView->isChecked())
        d->offset->getDocument()->recomputeFeature(d->offset);
}

void OffsetWidget::onModeTypeActivated(int val)
{
    d->offset->Mode.setValue(val);
    if (d->ui.updateView->isChecked())
        d->offset->getDocument()->recomputeFeature(d->offset);
}

void OffsetWidget::onJoinTypeActivated(int val)
{
    d->offset->Join.setValue((long)val);
    if (d->ui.updateView->isChecked())
        d->offset->getDocument()->recomputeFeature(d->offset);
}

void OffsetWidget::onIntersectionToggled(bool on)
{
    d->offset->Intersection.setValue(on);
    if (d->ui.updateView->isChecked())
        d->offset->getDocument()->recomputeFeature(d->offset);
}

void OffsetWidget::onSelfIntersectionToggled(bool on)
{
    d->offset->SelfIntersection.setValue(on);
    if (d->ui.updateView->isChecked())
        d->offset->getDocument()->recomputeFeature(d->offset);
}

void OffsetWidget::onFillOffsetToggled(bool on)
{
    d->offset->Fill.setValue(on);
    if (d->ui.updateView->isChecked())
        d->offset->getDocument()->recomputeFeature(d->offset);
}

void OffsetWidget::onUpdateViewToggled(bool on)
{
    if (on) {
        d->offset->getDocument()->recomputeFeature(d->offset);
    }
}

bool OffsetWidget::accept()
{
    try {
        double offsetValue = d->ui.spinOffset->value().getValue();
        Gui::cmdAppObjectArgs(d->offset, "Value = %f", offsetValue);
        d->ui.spinOffset->apply();
        Gui::cmdAppObjectArgs(d->offset, "Mode = %d", d->ui.modeType->currentIndex());
        Gui::cmdAppObjectArgs(d->offset, "Join = %d", d->ui.joinType->currentIndex());
        Gui::cmdAppObjectArgs(d->offset, "Intersection = %s", d->ui.intersection->isChecked() ? "True" : "False");
        Gui::cmdAppObjectArgs(d->offset, "SelfIntersection = %s", d->ui.selfIntersection->isChecked() ? "True" : "False");
        Gui::cmdAppObjectArgs(d->offset, "Fill = %s", d->ui.fillOffset->isChecked() ? "True" : "False");

        Gui::Command::doCommand(Gui::Command::Doc,"App.ActiveDocument.recompute()");
        if (!d->offset->isValid())
            throw Base::CADKernelError(d->offset->getStatusString());
        Gui::Command::doCommand(Gui::Command::Gui,"Gui.ActiveDocument.resetEdit()");
        Gui::Command::commitCommand();
    }
    catch (const Base::Exception& e) {
        QMessageBox::warning(this, tr("Input error"), QCoreApplication::translate("Exception", e.what()));
        return false;
    }

    return true;
}

bool OffsetWidget::reject()
{
    // get the support and Sketch
    App::DocumentObject* source = d->offset->Source.getValue();
    if (source){
        Gui::Application::Instance->getViewProvider(source)->show();
    }

    // roll back the done things
    Gui::Command::abortCommand();
    Gui::Command::doCommand(Gui::Command::Gui,"Gui.ActiveDocument.resetEdit()");
    Gui::Command::updateActive();

    return true;
}

void OffsetWidget::changeEvent(QEvent *e)
{
    QWidget::changeEvent(e);
    if (e->type() == QEvent::LanguageChange) {
        d->ui.retranslateUi(this);
    }
}


/* TRANSLATOR PartGui::TaskOffset */

TaskOffset::TaskOffset(Part::Offset* offset)
{
    widget = new OffsetWidget(offset);
    addTaskBox(Gui::BitmapFactory().pixmap("Part_Offset"), widget);
}

TaskOffset::~TaskOffset() = default;

Part::Offset* TaskOffset::getObject() const
{
    return widget->getObject();
}

void TaskOffset::open()
{
}

void TaskOffset::clicked(int)
{
}

bool TaskOffset::accept()
{
    return widget->accept();
}

bool TaskOffset::reject()
{
    return widget->reject();
}

#include "moc_TaskOffset.cpp"
