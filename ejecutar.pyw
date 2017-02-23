from cx_Freeze import setup, Executable

setup(name="SWAdhInformesDespachos",
      version= "1.1",
      description="El SW se encarga de mostrar los informes de despachos de la empresa",
      executables=[Executable("Adh-InformesDespachos.pyw")],)
