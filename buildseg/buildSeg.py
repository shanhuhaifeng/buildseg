# -*- coding: utf-8 -*-
"""
/***************************************************************************
 buildSeg
                                 A QGIS plugin
 Deep learning building segmentation
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2021-11-01
        git sha              : $Format:%H$
        copyright            : (C) 2021 by geoyee
        email                : geoyee@yeah.net
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QFileDialog
# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .buildSeg_dialog import buildSegDialog
import os.path
# tools
from qgis.utils import iface
from qgis.core import QgsMapLayerType
from .utils import *


class buildSeg:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'buildSeg_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&buildSeg')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

        self.infer_worker = None

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('buildSeg', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/buildSeg/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'buildseg bar'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&buildSeg'),
                action)
            self.iface.removeToolBarIcon(action)


    # 加载参数
    def select_params_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg, "选择参数路径", "", "*.pdparams")
        self.dlg.edtParams.setText(filename)
        if self.infer_worker is not None:
            self.infer_worker.load_params(filename)
            print("成功加载参数")


    def run(self):
        """Run method that performs all the real work"""

        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started
        if self.first_start == True:
            self.first_start = False
            self.dlg = buildSegDialog()
            # 初始化
            self.infer_worker = None
        # 添加事件
        self.dlg.btnParams.clicked.connect(self.select_params_file)

        # show the dialog
        self.dlg.show()
        self.infer_worker = InferWorker(self.dlg.cmbModel.currentText().lower())
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            layers = iface.activeLayer()  # 获取当前激活图层
            proj = layers.crs()
            grid_size = [512, 512]
            overlap = [24, 24]
            # 若此图层为栅格图层
            if layers.type() == QgsMapLayerType.RasterLayer:
                xsize, ysize = layers.width(), layers.height()
                grid_count, mask_grids = create_grids(ysize, xsize, grid_size, overlap)
                number = grid_count[0] * grid_count[1]
                print("开始分块处理")
                for i in range(grid_count[0]):
                    for j in range(grid_count[1]):
                        img = layer2array(layers, i, j, grid_size, overlap)
                        mask_grids[i][j] = self.infer_worker.get_mask(img)
                        print(f"-- {i * grid_count[0] + j + 1}/{number} --")
                print("开始拼接")
                mask = splicing_grids(mask_grids, ysize, xsize, grid_size, overlap)
                # test
                # import cv2
                # cv2.imwrite(r"E:\PdCVSIG\github\images\rs_img\test.png", mask)
                print("开始提取边界")
                build_bound = bound2shp(get_polygon(mask), 
                                        get_transform(layers))
                showgeoms([build_bound], "build_bound", proj=proj)
            else:
                print("当前活动图层非栅格图层")