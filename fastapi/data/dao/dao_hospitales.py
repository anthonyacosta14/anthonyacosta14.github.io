from data.modelo.hospital import Hospital

class DaoHospitales:
    
    def get_all(self,db) -> list[Hospital]:
        cursor = db.cursor()
    
        cursor.execute("SELECT * FROM hospitales")

        hospitales_en_db = cursor.fetchall()
        hospitales : list[Hospital]= list()
        for hospital in hospitales_en_db:
            alumno = Hospital(hospital[0], hospital[1], hospital[2])
            hospitales.append(alumno)
        cursor.close()
        
        return hospitales
    
    def insert(self, db, nombre: str, numero_pacientes: int):
        cursor = db.cursor()
        sql = ("INSERT INTO hospitales (nombre,numero_pacientes) values (%s,%s) ")
        data = (nombre,numero_pacientes)
        cursor.execute(sql,data)
        # cursor.execute(f"INSERT INTO hospitales (nombre) VALUES ('{nombre}')")
        db.commit()
        cursor.close()

    def delete(self, db, id: str):
        cursor = db.cursor()
        sql = ("DELETE FROM  hospitales where id = (%s) ")
        data = (id,)
        cursor.execute(sql,data)
        # cursor.execute(f"DELETE INTO hospitales (nombre) VALUES ('{nombre}')")
        db.commit()
        cursor.close()
    
    def update(self, db, id: int, nombre: str, numero_pacientes: int):
        cursor = db.cursor()
        sql = "UPDATE hospitales SET nombre = %s, numero_pacientes =%s WHERE id = %s"
        cursor.execute(sql, (nombre, numero_pacientes, id))
        db.commit()
        cursor.close()