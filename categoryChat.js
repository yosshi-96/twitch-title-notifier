const tmi = require('tmi.js');
var flg;
var id;
// Define configuration options
// twitch token -u -s 'chat:read chat:edit'
const opts = {
  identity: {
    username: 'oruorubot',
    password: 'oauth:gicf362ig3d7u81t7gebst0tf00c0h'
  },
  channels: [
    process.argv[3] 
  ],
  connection: [
    reconnect = false,
    maxReconnectAttempts = '1'
  ]
};

// Create a client with our options
const client = new tmi.client(opts);

// Connect to Twitch:
client.connect();
client.on('connected', onConnectedHandler);
client.on('error', test);

// Called every time the bot connects to Twitch chat
function onConnectedHandler (addr, port) {
  const args  = process.argv
  //動作しない場合はcommand.js内の　if(!hasFulfilled)処理を変える{ reject(err); }
  test = client.say('#' + process.argv[3] , `おっ今日は` + process.argv[2] + 'か');
}

// Called every time the bot connects to Twitch chat
function test (addr, port) {
  console.log('test')
}
