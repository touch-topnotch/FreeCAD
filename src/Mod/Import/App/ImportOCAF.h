/***************************************************************************
 *   Copyright (c) 2013 Werner Mayer <wmayer[at]users.sourceforge.net>     *
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

#ifndef IMPORT_IMPORTOCAF_H
#define IMPORT_IMPORTOCAF_H

#include <map>
#include <set>
#include <string>
#include <unordered_map>
#include <vector>

#include <Quantity_ColorRGBA.hxx>
#include <TDocStd_Document.hxx>
#include <TopoDS_Shape.hxx>
#include <XCAFDoc_ColorTool.hxx>
#include <XCAFDoc_ShapeTool.hxx>

#include <App/Part.h>
#include <Mod/Import/ImportGlobal.h>


class TDF_Label;
class TopLoc_Location;

namespace App
{
class Document;
class DocumentObject;
}  // namespace App
namespace Part
{
class Feature;
}

namespace Import
{

class ImportExport ImportOCAF
{
public:
    ImportOCAF(Handle(TDocStd_Document) h, App::Document* d, const std::string& name);
    virtual ~ImportOCAF();
    void loadShapes();
    void setMerge(bool);

private:
    void loadShapes(const TDF_Label& label,
                    const TopLoc_Location&,
                    const std::string& partname,
                    const std::string& assembly,
                    bool isRef,
                    std::vector<App::DocumentObject*>&);
    void createShape(const TDF_Label& label,
                     const TopLoc_Location&,
                     const std::string&,
                     std::vector<App::DocumentObject*>&,
                     bool);
    void createShape(const TopoDS_Shape& label,
                     const TopLoc_Location&,
                     const std::string&,
                     std::vector<App::DocumentObject*>&);
    void loadColors(Part::Feature* part, const TopoDS_Shape& aShape);
    virtual void applyColors(Part::Feature*, const std::vector<Base::Color>&)
    {}
    static void tryPlacementFromLoc(App::GeoFeature*, const TopLoc_Location&);
    static void tryPlacementFromMatrix(App::GeoFeature*, const Base::Matrix4D&);

private:
    Handle(TDocStd_Document) pDoc;
    App::Document* doc;
    Handle(XCAFDoc_ShapeTool) aShapeTool;
    Handle(XCAFDoc_ColorTool) aColorTool;
    bool merge {true};
    std::string default_name;
    std::set<int> myRefShapes;
};

class ImportExport ImportOCAFCmd: public ImportOCAF
{
public:
    ImportOCAFCmd(Handle(TDocStd_Document) h, App::Document* d, const std::string& name);
    std::map<Part::Feature*, std::vector<Base::Color>> getPartColorsMap() const
    {
        return partColors;
    }

private:
    void applyColors(Part::Feature* part, const std::vector<Base::Color>& colors) override;

private:
    std::map<Part::Feature*, std::vector<Base::Color>> partColors;
};

class ImportXCAF
{
public:
    ImportXCAF(Handle(TDocStd_Document) h, App::Document* d, const std::string& name);
    virtual ~ImportXCAF();
    void loadShapes();

private:
    void createShape(const TopoDS_Shape& shape, bool perface = false, bool setname = false) const;
    void loadShapes(const TDF_Label& label);
    virtual void applyColors(Part::Feature*, const std::vector<Base::Color>&)
    {}

private:
    Handle(TDocStd_Document) hdoc;
    App::Document* doc;
    Handle(XCAFDoc_ShapeTool) aShapeTool;
    Handle(XCAFDoc_ColorTool) hColors;
    std::string default_name;
    std::map<Standard_Integer, TopoDS_Shape> mySolids;
    std::map<Standard_Integer, TopoDS_Shape> myShells;
    std::map<Standard_Integer, TopoDS_Shape> myCompds;
    std::map<Standard_Integer, TopoDS_Shape> myShapes;
    std::map<Standard_Integer, Quantity_ColorRGBA> myColorMap;
    std::map<Standard_Integer, std::string> myNameMap;
};

}  // namespace Import

#endif  // IMPORT_IMPORTOCAF_H
