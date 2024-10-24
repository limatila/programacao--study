use("provaScript10")
db.createCollection("Cameras")
db.createCollection("Videos")
db.createCollection("Eventos")
db.createCollection("Alames")
db.createCollection("Usuarios")

db.Cameras.insertMany([
    {id: 2, localizacao: "Fortaleza", tipo: 'M', dataInstalacao: "2024-06-01", status: 'A' },
    {id: 5, localizacao: "Recife", tipo: 'A', dataInstalacao: "2024-06-01", status: 'I' },
    {id: 6, localizacao: "Alagoas", tipo: 'C', dataInstalacao: "2023-05-01", status: 'A' },
])

db.Videos.insertMany([
    {id: 1, dataHora: "2021-01-23", duracao: 20, camera: 2, status: 'A' },
    {id: 2, dataHora: "2021-01-22", duracao: 24, camera: 5, status: 'U' },
    {id: 3, dataHora: "2021-01-21", duracao: 762, camera: 6, status: 'A' },
])

db.Eventos.insertMany([
    {id: 12001, tipoEvento: 'G', dataHora: "2021-12-02", videoId: 2, status: 'A'},
    {id: 111, tipoEvento: 'P', dataHora: "2021-12-01", videoId: 1, status: 'A'},
    {id: 10, tipoEvento: 'M', dataHora: "2021-12-04", videoId: 3, status: 'A'},
])

db.Alarmes.insertMany([
    {id: 3, tipoAlarme: 'N', dataHora: "2021-12-01", cameraId: 5, status: 'A'},
    {id: 2, tipoAlarme: 'M', dataHora: "2021-12-02", cameraId: 2, status: 'A'},
    {id: 1, tipoAlarme: 'M', dataHora: "2021-12-03", cameraId: 6, status: 'A'},
])

db.Usuarios.insertMany([
    {id: 1, nome: "Breno", email: "breno.guima@yahoo.com.br", senha: 123, perfil: "admin"},
    {id: 2, nome: "Átila", email: "atilalimade@gmail.com", senha: 333, perfil: "user"},
    {id: 3, nome: "Fulano", email: "fulano@gmail.com", senha: 3223, perfil: "user"},
])

//finds
db.Videos.find({dataHora: "2021-01-23", camera: 2}) //Todos os vídeos de uma data e uma camera
db.Eventos.find({dataHora: "2021-12-01", videoId: 1}) //Todos os eventos de um video em uma data
db.Usuarios.find({perfil: "admin"}) //Todos os usuários com o perfil admin
