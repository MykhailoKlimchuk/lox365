# LibreOffice 7.4 on Windows bundles Python 3.8, so import from __future__
# in order to use new type hinting.
# https://peps.python.org/pep-0585/
from __future__ import annotations

import uno
import unohelper
from org.openoffice.sheet.addin import XLox365
import lox365 as lx

class Lox365(unohelper.Base, XLox365):
    def __init__(self, ctx): self.ctx = ctx

    def TBACC(self, *args):
        desktop = self.ctx.ServiceManager.createInstanceWithContext(
            "com.sun.star.frame.Desktop", self.ctx)

        model = desktop.getCurrentComponent()

        oSheet = model.getSheets().getByIndex(1)  # technical sheet

        audit_id_cell = oSheet.getCellRangeByName("A1")
        token_cell = oSheet.getCellRangeByName("A2")
        host_cell = oSheet.getCellRangeByName("A3")
        return lx.tbacc(audit_id_cell.String, token_cell.String, host_cell.String, *args)


def createInstance(ctx):
    return Lox365(ctx)

g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationHelper.addImplementation(
    createInstance, 'com.goosepirate.lox365.oxt',
    ('com.sun.star.sheet.AddIn',),)