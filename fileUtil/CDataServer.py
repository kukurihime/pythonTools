#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 18:23:01 2022

@author: kukurihime
"""
import subprocess
import os
import pathlib
import CStringUtil
import CFileUtil
import shutil

class CDataServer():
    def __init__(self, path = "./"):
        self.databaseServer = path
        self.mountPath = ""
        self.local = True
        self.accessMode = "serverPath"
        self.mountMode = "bash"
        self.mountSh = ""
        self.mountPos = 2
        self.passwd = ""
        self.errMsg = ""
        
        
    def setMountPath(self, path):
        if os.path.exists(path):
            self.mountPath = path
            self.clearError()
            return True
        else:
            self.errMsg = "setMountPath:Path is not exists!"
            return False
        
    def setMountShell(self, shellCmd):
        self.mountSh = shellCmd
    
    def setPassword(self, password):
        self.passwd = password
        
    def accessMode_mount(self):
        self.accessMode = "mount"
        
    def accessMode_serverPath(self):
        self.accessMode = "serverPath"
        
    def connectServer(self):
        if self.accessMode == "serverPath":
            #ready
            self.errmsg = "connectServer:Now ready..."
            return False
        elif self.accessMode == "mount":
            if self.checkConnect():
                self.errMsg = "connectServer:Already Mounted!"
                return False
        
            if self.mountMode == "bash":
                if self.mountSh == "":
                    self.errMsg = "connectServer:Mount Shell is not set!"
                    return False
                else:
                    cmd = [self.mountSh, self.passwd]
                    subprocess.run(cmd)
                    self.clearError()
                    return True
        
        
    def checkConnect(self):
        if self.accessMode == "mount":
            osRet = subprocess.run(['mount'], capture_output = True, text = True)
            su = CStringUtil.CStringUtil()
            osRet = osRet.stdout
            osRet = su.splitMatrixBy( osRet, ' ')
            osRet = su.columnInMatrix( osRet, self.mountPos)
        
            absoluteMountPath = str(pathlib.Path( self.mountPath ).resolve())

            for pos in osRet:
                if pos == absoluteMountPath:
                    self.clearError()
                    return True
                else:
                    pass
            
            return False
    
    def copyToServer(self, origin):
        self.connectServer()
        #move
        targetPath = self.targetPath()
        if os.path.exists(origin):
            dest = targetPath + origin
                        
            shutil.copy(origin, dest)
            
    def removeCopiedOriginalFile(self, originalPath):
        self.connectServer()
        fu = CFileUtil.CFileUtil()
        
        copiedFileList = fu.getSameFilenameList(originalPath, self.targetPath())
        for file in copiedFileList:
            if fu.isSameFile(file, self.targetPath() + file):
                if os.path.isfile(originalPath+ file):
                    os.remove(originalPath + file)
                    
    def targetPath(self):
        if self.accessMode == "serverPath":
            return self.databaseServer
        elif self.accessMode == "mount":
            return self.mountPath
        else:
            return False
    
    def errorMessage(self):
        return self.errMsg
    
    def clearError(self):
        self.errMsg = ""
        
            
if __name__ == "__main__":
    print('CDataServer Test')
    ds = CDataServer()
    mountPath = '/home/kukurihime/networkPublic/dirac_binanceUSB'
    ds.setMountPath(mountPath)
    print(ds.mountPath)
    ret = ds.checkMount()
    print(ret)    
    ds.connectServer()
    print( ds.errorMessage())
        
        