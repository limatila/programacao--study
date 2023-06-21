clients_logged = {      //cada id tem: name, interested_in, location, SHOULD have ip
    'ObjName': 'Clientes Logados',

    "id_00001": {
        'name': 'johansen',
        'interested_in': ['art', 'classical music', 'math'],
        'location': 'England'
    },
    
    'id_00002': {
        'name': 'biel',
        'interested_in': ['funk', 'futmesa'],
        'location': 'Rio de Janeiro - RJ'
    },

    'id_00003': {
        'name': 'gabu',
        'interested_in': ['MCR', 'psichology', 'Genshim Impact', 'Roblox'],
        'location': 'Parque Araxá, Fort- Ce'
    },

    'id_00004': {
        'name': 'lolecoisadecorno',
        'interested_in': ['streaming', 'udyr', 'tiny indie games', 'funk pesadaum'],
        'location': undefined
    },
}

function genRandomId(){
    soma = Math.floor(Math.random() * 100000)
    id_str = String('id_' + soma)
    console.log('User id set to: ' + id_str + '...')
    return id_str
}
//1: adicionar um user
function addUser(dataObj, num_id, username, user_Interesse, userLocation, ){
    
    if (num_id === false || null || undefined){
        throw console.error('Can\'t create without a id number, specify one or set \'true\' to get a random one');
    } else if (num_id === true){
        num_id = genRandomId()

    } else if(num_id === 'ObjName'){
        throw console.error('The object name can\'t be changed.')

    } else if(num_id === "id_"){
        throw console.error('Specify an id correctly: \'id_XXXXX\' / \'true\' / \'false\'')

    } else if(num_id.startsWith('id_') === false){  //num_id como função se colocar um int????
        throw console.error('Specify an id correctly: \'id_XXXXX\' / \'true\' / \'false\'')
    }   //if true, should make a random id, if missing 'id_', should ask to correct it
    
    
    //if already existant, choose other id
    if(dataObj[num_id] !== undefined || null || false){
        console.log("id já existe!, um novo irá ser gerado...")
        num_id = genRandomId()
        dataObj[num_id] = {
            'name': username,
            'interested_in': user_Interesse,
            'location': userLocation,
        }
    } else {
        dataObj[num_id] = {
                'name': username,
                'interested_in': user_Interesse,
                'location': userLocation,
            }
    }
    
    console.log('Usuário logado com sucesso')
}

function makeCopy(objName){
    copy1 = JSON.parse(JSON.stringify(objName)); 
    console.log(copy1) 
    console.log('cópia acima! ☝☝')
}

addUser(clients_logged, 'id_00002', 'sapinho', ['musica', 'bateria', 'jogos indie', ], 'Parquelandia, Fort - CE')
makeCopy(clients_logged)

//addUser(clients_logged, 'id_00004', 'alesson', ['rock', 'apartamentos por temporada', 'praia'], 'Minha casa')   //se uma mudança foi feita, valerá pra todas as instancias de 'console.log'


//2: remover um user
function removeUser(dataObj, num_id){

    if(num_id == 'all') {
        delete dataObj; console.log(dataObj.ObjName + ' was erased sucessfully!')
    } else if (num_id.startsWith('id_') == true){ 
        delete dataObj[num_id]; console.log(num_id + ' was erased sucessfully!')
    } else {
        throw console.error('Specify an id correctly: \'id_XXXXX\' / \'all\'')
    }
}

//3: mudar uma prop. (add, remove, change)
function changeProp(objName, num_id, idProp, value){
    if(num_id === 'ObjName'){
        console.error('The object name can\'t be changed.')
    } else if (value === 'del'){
        delete objName[num_id][idProp]
        console.log("id prop deleted sucessfully!")
    } else if (idProp === 'name'){
        console.warn("WARNING: it\'s not safe to change name of id. for precaution: it\'s " + num_id + " and the name was " + objName[num_id][idProp])
        objName[num_id][idProp] = value
        console.log("name of User changed sucessfully!")
    } else {
        objName[num_id][idProp] = value
        console.log("id prop changed sucessfully!")
    } 
}


//4: 