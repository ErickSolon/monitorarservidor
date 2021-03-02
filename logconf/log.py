class logrun():
    def __init__(self, datahora, dequem, paraquem):
        self.datahora = datahora
        self.dequem = dequem
        self.paraquem = paraquem

    def gravar(self):
        try:
            with open("log.txt", "a+") as logg:
                logg.seek(0)
                logg.writelines("HORA DO ENVIO DE E-MAIL: " + self.datahora + "\n" +
                                "E-MAIL SERVIDOR: " + self.dequem + "\n" +
                                "E-MAIL CLIENTE :" + self.dequem + "\n"
                                )
        except Exception as e:
            print("gravar error:",  e)
        finally:
            logg.close()
