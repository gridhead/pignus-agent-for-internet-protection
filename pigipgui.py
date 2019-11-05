from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys, time, pigip_urlsca, pigip_urlrep, pigip_domrep

ui,_=loadUiType('pigip.ui')
aknf_title="API Key Not Found"
aknf_mesge="This functionality of the application requires a valid VirusTotal API key. "+\
           "Signup for a free API key and copy it into a text file called 'virustotal.key'. "+\
           "Store this file in the application root directory. Retry now?"
urnf_title="Scanning has failed"
urnf_mesge="Fret not. Try doing the following things to ensure the smooth working\n"+\
           "- Check the URL once again for typographical mistakes\n"+\
           "- Check the validity of the API key with your VirusTotal account\n"+\
           "- Check if the domain has not been blocked by your ISP\n"+\
           "- Try queueing the URL scan again and wait before checking the results"

class MainApp(QMainWindow,ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.title = 'Pignus Agent for Internet Protection v0.01 by t0xic0der'
        self.setupUi(self)
        self.handle_elements()

    def handle_elements(self):
        self.setWindowTitle(self.title)
        self.urlsca_scadat_res.setReadOnly(True)
        self.urlsca_scarsc_res.setReadOnly(True)
        self.urlsca_scanid_res.setReadOnly(True)
        self.urlsca_scaper_res.setReadOnly(True)
        self.urlrep_scanid_res.setReadOnly(True)
        self.urlrep_scaurl_res.setReadOnly(True)
        self.urlrep_scadat_res.setReadOnly(True)
        self.domrep_whotim_res.setReadOnly(True)
        self.domrep_dnsrec_res.setReadOnly(True)
        self.domrep_scadat_res.setReadOnly(True)
        self.urlsca_btn.clicked.connect(self.queueUrlScanning)
        self.urlrep_btn.clicked.connect(self.retriveUrlReport)
        self.domrep_btn.clicked.connect(self.retriveDomReport)

    def queueUrlScanning(self):
        scannable=self.urlsca_box.text()
        try:
            self.urlsca_scadat_res.clear()
            self.urlsca_scarsc_res.clear()
            self.urlsca_scanid_res.clear()
            self.urlsca_scaper_res.clear()
            start_time=time.time()
            reply=pigip_urlsca.main(scannable)
            end_time=time.time()
            total_time = str((end_time - start_time)/60)
            time_array=total_time.split(".")
            total_time=time_array[0]+"."+time_array[1][0:2]
            self.urlsca_scadat_res.setText(reply[3])
            self.urlsca_scarsc_res.setText(reply[2])
            self.urlsca_scanid_res.setText(reply[4])
            self.urlsca_scaper_res.setText(reply[1])
            self.urlsca_apires_res.setText(reply[0])
            self.urlsca_scares_res.setText(reply[5])
            self.contri.setText("Result fetched in "+total_time+" minutes")
        except FileNotFoundError:
            warn=QMessageBox.warning(self,aknf_title,aknf_mesge,QMessageBox.Yes|QMessageBox.No)
            if warn==QMessageBox.Yes:
                self.queueUrlScanning()
            if warn==QMessageBox.No:
                exit(0)
        except Exception:
            self.urlsca_scadat_res.clear()
            self.urlsca_scarsc_res.clear()
            self.urlsca_scanid_res.clear()
            self.urlsca_scaper_res.clear()
            warn = QMessageBox.warning(self, urnf_title, urnf_mesge, QMessageBox.Ok)

    def retriveUrlReport(self):
        scannable=self.urlrep_box.text()
        try:
            self.urlrep_scanid_res.clear()
            self.urlrep_scaurl_res.clear()
            self.urlrep_scadat_res.clear()
            start_time = time.time()
            reply = pigip_urlrep.main(scannable)
            end_time = time.time()
            total_time = str((end_time - start_time)/60)
            time_array = total_time.split(".")
            total_time = time_array[0] + "." + time_array[1][0:2]
            self.urlrep_scanid_res.setText(reply[5])
            self.urlrep_scaurl_res.setText(reply[3])
            self.urlrep_scadat_res.setText(reply[4])
            self.urlrep_scares_res.setText(reply[6])
            self.totale_res.setText(reply[1])
            self.postev_res.setText(reply[2])
            data=reply[0]
            if data:
                self.detact_teb.setRowCount(0)
                self.detact_teb.insertRow(0)
                for row, form in enumerate(data):
                    for column, item in enumerate(form):
                        self.detact_teb.setItem(row, column, QTableWidgetItem(str(item)))
                        column += 1
                    row_position = self.detact_teb.rowCount()
                    self.detact_teb.insertRow(row_position)
            self.contri.setText("Result fetched in " + total_time + " minutes")
        except FileNotFoundError:
            warn = QMessageBox.warning(self, aknf_title, aknf_mesge, QMessageBox.Yes | QMessageBox.No)
            if warn == QMessageBox.Yes:
                self.queueUrlScanning()
            if warn==QMessageBox.No:
                exit(0)
        except Exception:
            self.urlrep_scanid_res.clear()
            self.urlrep_scaurl_res.clear()
            self.urlrep_scadat_res.clear()
            warn = QMessageBox.warning(self, urnf_title, urnf_mesge, QMessageBox.Ok)

    def retriveDomReport(self):
        scannable=self.domrep_box.text()
        try:
            self.domrep_whotim_res.clear()
            self.domrep_dnsrec_res.clear()
            self.domrep_scadat_res.clear()
            start_time = time.time()
            reply = pigip_domrep.main(scannable)
            end_time = time.time()
            total_time = str((end_time - start_time)/60)
            time_array = total_time.split(".")
            total_time = time_array[0] + "." + time_array[1][0:2]
            self.domrep_apires_res.setText(reply[0])
            self.domrep_whoisd_res.setText(reply[1])
            subsibli,resolist,whoistab=reply[2],reply[3],reply[4]
            self.domrep_whotim_res.setText(reply[5])
            self.domrep_dnsrec_res.setText(reply[6])
            self.domrep_scadat_res.setText(reply[7])
            self.domrep_scares_res.setText(reply[8])
            if resolist:
                self.domrep_resdat_teb.setRowCount(0)
                self.domrep_resdat_teb.insertRow(0)
                for row, form in enumerate(resolist):
                    for column, item in enumerate(form):
                        self.domrep_resdat_teb.setItem(row, column, QTableWidgetItem(str(item)))
                        column += 1
                    row_position = self.domrep_resdat_teb.rowCount()
                    self.domrep_resdat_teb.insertRow(row_position)
            if subsibli:
                self.domrep_subdom_teb.setRowCount(0)
                self.domrep_subdom_teb.insertRow(0)
                for row, form in enumerate(subsibli):
                    for column, item in enumerate(form):
                        self.domrep_subdom_teb.setItem(row, column, QTableWidgetItem(str(item)))
                        column += 1
                    row_position = self.domrep_subdom_teb.rowCount()
                    self.domrep_subdom_teb.insertRow(row_position)
            if whoistab:
                self.domrep_whodat_teb.setRowCount(0)
                self.domrep_whodat_teb.insertRow(0)
                for row, form in enumerate(whoistab):
                    for column, item in enumerate(form):
                        self.domrep_whodat_teb.setItem(row, column, QTableWidgetItem(str(item)))
                        column += 1
                    row_position = self.domrep_whodat_teb.rowCount()
                    self.domrep_whodat_teb.insertRow(row_position)
            self.contri.setText("Result fetched in " + total_time + " minutes")
        except FileNotFoundError:
            warn = QMessageBox.warning(self, aknf_title, aknf_mesge, QMessageBox.Yes | QMessageBox.No)
            if warn == QMessageBox.Yes:
                self.queueUrlScanning()
            if warn == QMessageBox.No:
                exit(0)
        except Exception:
            self.domrep_resdat_teb.setRowCount(0)
            self.domrep_subdom_teb.setRowCount(0)
            self.domrep_whodat_teb.setRowCount(0)
            self.domrep_whotim_res.clear()
            self.domrep_dnsrec_res.clear()
            self.domrep_scadat_res.clear()
            warn = QMessageBox.warning(self, urnf_title, urnf_mesge, QMessageBox.Ok)

def main():
    app=QApplication(sys.argv)
    QFontDatabase.addApplicationFont("fonts/Comfortaa-Bold.ttf")
    QFontDatabase.addApplicationFont("fonts/Comfortaa-Light.ttf")
    QFontDatabase.addApplicationFont("fonts/Comfortaa-Regular.ttf")
    QFontDatabase.addApplicationFont("fonts/Roboto-Bold.ttf")
    QFontDatabase.addApplicationFont("fonts/Roboto-Light.ttf")
    window=MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
