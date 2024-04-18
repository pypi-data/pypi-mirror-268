import os
import sys
import csv
import glob
import json
import time
import shutil
import openpyxl
from log_analysis_tool.ui import Mainui
from datetime import datetime
from PyQt5.QtCore import QTimer, QStringListModel
from easydict import EasyDict as edict
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox, QAbstractItemView

class Fun(Mainui):
    def __init__(self):
        super().__init__()
        self.setupUi()
        
        self.input_dt_start.setDateTime(self.get_datetime())
        self.input_dt_end.setDateTime(self.get_datetime())
        self.clean_result_uuid_list = []
        self.send_rcc_uuid_list = []
        self.base_img_label = {"large_garbage": "垃圾", "garbage": "垃圾", "sewage": "脏污", "mixed_garbage_temp": "固液混合"}
        self.csv_data = {}
        self.logfiles = []
        self.table_head = ['UUID', '标签', '中文标签', '图片名', '时间']

        # self.statusLabel = QLabel("") # 已清扫: 0 个 || 已上报: 0 个
        # self.statusBar().addPermanentWidget(self.statusLabel)

        self.show()

        # tab1 -> process log
        self.btn_log.clicked.connect(self.get_log_file_path) # load : log -> img -> csv
        self.btn_site_save.clicked.connect(self.get_save_result_path)
        self.btn_save.clicked.connect(self.save_result_file)
        #tab2 -> find and move info.csv
        self.btn_file.clicked.connect(self.tab2_get_info_csv_path)
        self.btn_save_2.clicked.connect(self.tab2_set_info_csv_save_path)
        self.btn_move.clicked.connect(self.tab2_find_and_move_info_csv)
        # tat changed
        self.tabWidget.currentChanged.connect(self.tab_change)

    #----------------------------------------------Process Log----------------------------------------------------------------------
    def get_datetime(self):
        return datetime.now()

    def timestamp_to_datetime(self, timestamp:str):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(timestamp) / 1000))

    def get_log_file_path(self):
        reply = QMessageBox(QMessageBox.Information, self.tr("提示"), self.tr("请先填写时间范围 !"), QMessageBox.NoButton, self)
        yr_btn = reply.addButton(self.tr("已填写"), QMessageBox.YesRole)
        reply.addButton(self.tr("取消"), QMessageBox.NoRole)
        reply.exec_()
        if reply.clickedButton() == yr_btn:
            # 每次在加载数据的时候 先清空上次的数据
            self.remove_data()
            reply = QMessageBox(QMessageBox.Information, self.tr("提示"), self.tr("请加载 Log 所在目录 !"), QMessageBox.NoButton, self)
            yr_btn = reply.addButton(self.tr("好的"), QMessageBox.YesRole)
            reply.addButton(self.tr("取消"), QMessageBox.NoRole)
            reply.exec_()
            if reply.clickedButton() == yr_btn:
                path = QFileDialog.getExistingDirectory(self, "选择 Log 所在文件夹")
                if path != "":
                    self.input_log.setText(path)
                    QTimer.singleShot(1000, self.load_log_files)

    def get_save_result_path(self):
        path = QFileDialog.getExistingDirectory(self, "选择保存文件夹")
        if path != "":
            self.input_result.setText(path)

    def load_csv_file(self):
        file = QFileDialog.getExistingDirectory(self, "选择 info.csv 所在目录")

        if file != "":
            self.input_csv.setText(file)
            QTimer.singleShot(1000, self.read_csv_img)
        else:
            self.load_log_files()

        self.listen_path()

    def load_img_files(self):
        path = QFileDialog.getExistingDirectory(self, "选择图片文件夹")
        if path != "":
            self.input_img.setText(path)
        else:
            self.load_log_files()

        self.listen_path()
    
    def read_csv_img(self):
        try:
            data = {}

            csv_list = glob.glob(f'{self.input_csv.text()}\\**.csv')
            img_list = glob.glob(f'{self.input_img.text()}\\**')
            
            imglist = [item.split('.')[0] for dirl in img_list for item in os.listdir(dirl)]
            
            if len(imglist) == 0:
                self.input_img.setText("")
                reply = QMessageBox(QMessageBox.Warning, self.tr("警告"), self.tr("该目录下没有图片 !"), QMessageBox.NoButton, self)
                yr_btn = reply.addButton(self.tr("重新选择 图片 所在目录"), QMessageBox.YesRole)
                reply.addButton(self.tr("取消"), QMessageBox.NoRole)
                reply.exec_()
                if reply.clickedButton() == yr_btn:
                    self.load_csv_file()

            if len(csv_list) == 0:
                self.input_csv.setText("")
                reply = QMessageBox(QMessageBox.Warning, self.tr("警告"), self.tr("该目录下没有正确的 csv 文件 !"), QMessageBox.NoButton, self)
                yr_btn = reply.addButton(self.tr("重新选择 csv 所在目录"), QMessageBox.YesRole)
                reply.exec_()
                if reply.clickedButton() == yr_btn:
                    self.load_log_files()

            if len(csv_list) != 0 and len(imglist) != 0:
                for cit in csv_list:
                    self.show_message(f"正在加读取 {cit} 文件")
                    with open(cit, 'r', errors="ignore") as f:
                        reader = list(csv.reader(f))[1:]

                    for row in reader:
                        image_name = row[1]
                        class_name = row[2]
                        uuid = row[4]

                        if image_name in imglist:
                            data[uuid] = {"img_name": image_name, "class_name": class_name}
                self.csv_data = data
                
                self.show_message(f"csv 文件 和 图片 已读取完成")
                self.read_log_file()
        except BaseException as be:
            reply = QMessageBox(QMessageBox.Warning, self.tr("警告"), self.tr(str(be)), QMessageBox.NoButton, self)
            yr_btn = reply.addButton(self.tr("好的"), QMessageBox.YesRole)
            reply.addButton(self.tr("取消"), QMessageBox.NoRole)
            reply.exec_()
            if reply.clickedButton() == yr_btn:
                self.remove_data()
            else:
                self.remove_data()

    def load_log_files(self):
        if self.input_img.text() == "":
            reply = QMessageBox(QMessageBox.Question, self.tr("提示"), self.tr("请加载 图片 所在目录 !"), QMessageBox.NoButton, self)
            yr_btn = reply.addButton(self.tr("选择 图片 所在目录"), QMessageBox.YesRole)
            reply.addButton(self.tr("取消"), QMessageBox.NoRole)
            reply.exec_()
            if reply.clickedButton() == yr_btn:
                self.load_img_files()
            else:
                self.remove_data()

        if self.input_img.text() != "" and self.input_csv.text() == "":
            reply = QMessageBox(QMessageBox.Question, self.tr("提示"), self.tr("请加载 info.csv 所在目录 !"), QMessageBox.NoButton, self)
            yr_btn = reply.addButton(self.tr("选择 info.csv 所在目录"), QMessageBox.YesRole)
            reply.addButton(self.tr("取消"), QMessageBox.NoRole)
            reply.exec_()
            if reply.clickedButton() == yr_btn:
                self.load_csv_file()
            else:
                self.remove_data()

        if self.input_img.text() != "" and self.input_csv.text() != "":
            self.logfiles = glob.glob(f'{self.input_log.text()}/gs_console*.log')
            
            if len(self.logfiles) == 0:
                reply = QMessageBox(QMessageBox.Question, self.tr("提示"), self.tr("该目录下没有 console 日志 , 请重选目录"), QMessageBox.NoButton, self)
                yr_btn = reply.addButton(self.tr("重选"), QMessageBox.YesRole)
                reply.addButton(self.tr("取消"), QMessageBox.NoRole)
                reply.exec_()
                if reply.clickedButton() == yr_btn:
                    self.get_log_file_path()
                else:
                    self.remove_data()

            self.listen_path()
    
    def read_log_file(self):
        begin_time = datetime.strptime(self.input_dt_start.dateTime().toString('yyyy-MM-dd HH:mm:ss'), "%Y-%m-%d %H:%M:%S").timestamp()
        end_time = datetime.strptime(self.input_dt_end.dateTime().toString('yyyy-MM-dd HH:mm:ss'), "%Y-%m-%d %H:%M:%S").timestamp()
        for item in self.logfiles:
            self.show_message(f"正在加载 {item} 文件")
            with open(item, 'r', encoding='UTF-8', errors="ignore") as f:
                lines = f.readlines()
            for l in lines:
                if "[garbage_upload] send rcc" in l:
                    split_data = l.split(" ")
                    log_datetime_timestamp = datetime.strptime(f"{split_data[0]} {split_data[1].split('.')[0]}", "%Y-%m-%d %H:%M:%S").timestamp()
                    tmp = edict(json.loads(split_data[-1].replace("\n", "")))
                    t_l = [tmp.id, tmp.category]
                    if log_datetime_timestamp >= begin_time and log_datetime_timestamp <= end_time:
                        if t_l not in self.send_rcc_uuid_list:
                            self.send_rcc_uuid_list.append(t_l)

                if "clean_result(0)" in l:
                    split_data = l.split(" ")
                    log_datetime_timestamp = datetime.strptime(f"{split_data[0]} {split_data[1].split('.')[0]}", "%Y-%m-%d %H:%M:%S").timestamp()
                    tmp = split_data[-2].replace("dirty_id(", "").replace(")", "")
                    if log_datetime_timestamp >= begin_time and log_datetime_timestamp <= end_time:
                        if tmp not in self.clean_result_uuid_list:
                            self.clean_result_uuid_list.append(tmp)

        QTimer.singleShot(1000, lambda:self.show_message("加载 log 文件完成"))
        
        QTimer.singleShot(2000, self.show_label)

        QTimer.singleShot(3000, self.create_table)

    def create_table(self):
        length_clean_result = len(self.clean_result_uuid_list)
        model = QStandardItemModel(self.tableView)
        model.setHorizontalHeaderLabels(self.table_head)
        model.setColumnCount(5)
        model.setRowCount(length_clean_result)
        for i in range(length_clean_result):
            item1 = QStandardItem(self.clean_result_uuid_list[i])
            if self.clean_result_uuid_list[i] in self.csv_data:
                tmp_dict = edict(self.csv_data[self.clean_result_uuid_list[i]])
                self.clean_result_uuid_list[i] = [self.clean_result_uuid_list[i], tmp_dict.class_name, self.base_img_label[tmp_dict.class_name], tmp_dict.img_name, self.timestamp_to_datetime(tmp_dict.img_name)]
                item2 = QStandardItem(tmp_dict.class_name)
                item3 = QStandardItem(self.base_img_label[tmp_dict.class_name])
                item4 = QStandardItem(tmp_dict.img_name)
                item5 = QStandardItem(self.timestamp_to_datetime(tmp_dict.img_name))
            else:
                self.clean_result_uuid_list[i] = (self.clean_result_uuid_list[i], "", "", "", "")
                item2 = QStandardItem("")
                item3 = QStandardItem("")
                item4 = QStandardItem("")
                item5 = QStandardItem("")
            model.setItem(i, 0, item1)
            model.setItem(i, 1, item2)
            model.setItem(i, 2, item3)
            model.setItem(i, 3, item4)
            model.setItem(i, 4, item5)
        self.tableView.setModel(model)
        self.tableView.setColumnWidth(0, 300)
        self.tableView.setColumnWidth(4, 130)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.show()

        # ===========================================================

        length_send_rcc = len(self.send_rcc_uuid_list)
        model_2 = QStandardItemModel(self.tableView_1)
        model_2.setColumnCount(4)
        model_2.setRowCount(length_send_rcc)
        model_2.setHorizontalHeaderLabels(self.table_head)
        for i in range(length_send_rcc):
            tmp = self.send_rcc_uuid_list[i]
            tmp.append(self.base_img_label[tmp[1]])

            item1 = QStandardItem(tmp[0])
            item2 = QStandardItem(tmp[1])
            item3 = QStandardItem(tmp[2])
            if tmp[0] in self.csv_data:
                tmp.append(self.csv_data[tmp[0]]['img_name'])
                tmp.append(self.timestamp_to_datetime(self.csv_data[tmp[0]]['img_name']))
                item4 = QStandardItem(self.csv_data[tmp[0]]['img_name'])
                item5 = QStandardItem(self.timestamp_to_datetime(self.csv_data[tmp[0]]['img_name']))
            else:
                tmp.append("")
                tmp.append("")
                item4 = QStandardItem("")
                item5 = QStandardItem("")

            self.send_rcc_uuid_list[i] = tmp

            model_2.setItem(i, 0, item1)
            model_2.setItem(i, 1, item2)
            model_2.setItem(i, 2, item3)
            model_2.setItem(i, 3, item4)
            model_2.setItem(i, 4, item5)
        self.tableView_1.setModel(model_2)
        self.tableView_1.setColumnWidth(0, 300)
        self.tableView_1.setColumnWidth(4, 130)
        self.tableView_1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView_1.show()

    def show_message(self, msg):
        self.statusBar().showMessage(msg)
    
    def show_label(self):
        self.statusLabel.setText(f"已清扫:{len(self.clean_result_uuid_list)} 个 || 已上报: {len(self.send_rcc_uuid_list)} 个")

    def listen_path(self):
        log_dir = self.input_log.text()
        csv_dir = self.input_csv.text()
        img_dir = self.input_img.text()
        if log_dir != "" and csv_dir != "" and img_dir != "":
            self.btn_save.setDisabled(False)
        else:
            self.btn_save.setDisabled(True)

    def save_result_file(self):
        if self.input_result.text() == "":
            reply = QMessageBox(QMessageBox.Question, self.tr("提示"), self.tr("请选择结果保存目录 !"), QMessageBox.NoButton, self)
            yr_btn = reply.addButton(self.tr("选择保存目录"), QMessageBox.YesRole)
            reply.addButton(self.tr("取消"), QMessageBox.NoRole)
            reply.exec_()
            if reply.clickedButton() == yr_btn:
                self.get_save_result_path()
            else:
                self.input_result.setText("")
        else:
            workbook = openpyxl.Workbook()

            sheet = workbook.active
            sheet.title = "已清扫"

            sheet['A1'] = self.table_head[0]
            sheet['B1'] = self.table_head[1]
            sheet['C1'] = self.table_head[2]
            sheet['D1'] = self.table_head[3]
            sheet['E1'] = self.table_head[4]

            sheet.column_dimensions['A'].width = 40
            sheet.column_dimensions['B'].width = 15
            sheet.column_dimensions['D'].width = 15
            sheet.column_dimensions['E'].width = 20

            for it in self.clean_result_uuid_list:
                sheet.append(it)

            sheet2 = workbook.create_sheet("已上报")
            sheet2['A1'] = self.table_head[0]
            sheet2['B1'] = self.table_head[1]
            sheet2['C1'] = self.table_head[2]
            sheet2['D1'] = self.table_head[3]
            sheet2['E1'] = self.table_head[4]

            sheet2.column_dimensions['A'].width = 40
            sheet2.column_dimensions['B'].width = 15
            sheet2.column_dimensions['D'].width = 15
            sheet2.column_dimensions['E'].width =20
            

            for it in self.send_rcc_uuid_list:
                sheet2.append(it)

            try:
                workbook.save(f"{self.input_result.text()}/show.xlsx")
                reply = QMessageBox(QMessageBox.Question, self.tr("提示"), self.tr("已保存到该目录下, 名为 show.xlsx !"), QMessageBox.NoButton, self)
                yr_btn = reply.addButton(self.tr("确定"), QMessageBox.YesRole)
                reply.exec_()
            except PermissionError as pe:
                reply = QMessageBox(QMessageBox.Question, self.tr("警告"), self.tr(str(pe)), QMessageBox.NoButton, self)
                yr_btn = reply.addButton(self.tr("确定"), QMessageBox.YesRole)
                reply.exec_()

    def remove_data(self):
        self.input_log.setText("")
        self.input_csv.setText("")
        self.input_img.setText("")
        self.input_result.setText("")
        self.clean_result_uuid_list = []
        self.send_rcc_uuid_list = []
        self.csv_data = {}
        self.logfiles = []
        self.statusLabel.setText("已清扫: 0 个 || 已上报:0 个")
        model = QStandardItemModel(self.tableView)
        model1 = QStandardItemModel(self.tableView_1)
        model.clear()
        model1.clear()
        self.tableView.setModel(model)
        self.tableView.show()
        self.tableView_1.setModel(model1)
        self.tableView_1.show()
        self.btn_save.setDisabled(True)

    #----------------------------------------------Find and move info.csv----------------------------------------------------------------------
    def tab2_get_info_csv_path(self):
        path = QFileDialog.getExistingDirectory(self, "选择所有 info.csv 所在目录")
        if path != "":
            self.input_file.setText(path)
        else:
            self.tab2_remove_data()

    def tab2_set_info_csv_save_path(self):
        path = QFileDialog.getExistingDirectory(self, "选择 info.csv 保存目录")
        if path != "":
            self.input_save.setText(path)

    def tab2_find_and_move_info_csv(self):
        if self.input_file.text() == "":
            reply = QMessageBox(QMessageBox.Information, self.tr("提示"), self.tr("请先填写所有 info.csv 所在目录 !"), QMessageBox.NoButton, self)
            yr_btn = reply.addButton(self.tr("好的"), QMessageBox.YesRole)
            reply.addButton(self.tr("取消"), QMessageBox.NoRole)
            reply.exec_()
            if reply.clickedButton() == yr_btn:
                self.tab2_get_info_csv_path()
        elif self.input_save.text() == "":
            reply = QMessageBox(QMessageBox.Information, self.tr("提示"), self.tr("请先填写 info.csv 保存目录 !"), QMessageBox.NoButton, self)
            yr_btn = reply.addButton(self.tr("好的"), QMessageBox.YesRole)
            reply.addButton(self.tr("取消"), QMessageBox.NoRole)
            reply.exec_()
            if reply.clickedButton() == yr_btn:
                self.tab2_set_info_csv_save_path()
        else:
            self.btn_file.setDisabled(True)
            garbage_csv = [it for it in [os.sep.join([self.input_file.text(), dit, "garbage_sewage_mtl", "project_node", "garbage_instance_seg_proj_tracking", "info.csv"]) for dit in os.listdir(self.input_file.text())] if os.path.exists(it)]
            sewage_csv = [it for it in [os.sep.join([self.input_file.text(), dit, "garbage_sewage_mtl", "project_node", "sewage_semantic_seg_proj_tracking", "info.csv"]) for dit in os.listdir(self.input_file.text())] if os.path.exists(it)]
            info_csv_list = garbage_csv + sewage_csv
            
            slm = QStringListModel()
            slm.setStringList(info_csv_list)
            self.listView.setModel(slm)

            self.statusLabel.setText(f"共找到 {len(info_csv_list)} 个 info.csv 文件 !")

            if info_csv_list:
                index = 1
                for it in info_csv_list:
                    shutil.copy(it, os.path.join(self.input_save.text(), f"info{index}.csv"))
                    index += 1

                reply = QMessageBox(QMessageBox.Information, self.tr("提示"), self.tr(f"{len(info_csv_list)} 个 info.csv 文件已拷贝到该目录下 !"), QMessageBox.NoButton, self)
                yr_btn = reply.addButton(self.tr("确定"), QMessageBox.YesRole)
                reply.exec_()
            else:
                reply = QMessageBox(QMessageBox.Warning, self.tr("警告"), self.tr("该目录下没有 info.csv 文件 !"), QMessageBox.NoButton, self)
                yr_btn = reply.addButton(self.tr("确定"), QMessageBox.YesRole)
                reply.exec_()

            self.btn_file.setDisabled(False)
    
    def tab2_remove_data(self):
        self.input_file.setText("")
        self.input_save.setText("")

    #----------------------------------------------tab changed----------------------------------------------------------------------
    def tab_change(self):
        self.statusLabel.setText("")
        self.show_message("")

def main():
    app = QApplication(sys.argv)
    fun = Fun()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()