// Assuming you already have a web3 instance and the contract ABI and address

// First, get the contract instance
const contractInstance = new web3.eth.Contract(contractABI, contractAddress);

// Next, define the transaction parameters
const recipient = '0x123...'; // the Ethereum address of the recipient
const amount = '1000000000000000000'; // the amount of tokens to send, in wei (1 token = 10^18 wei)

// Call the `transfer` function on the contract instance, using the `send` method
contractInstance.methods.transfer(recipient, amount).send({ from: senderAddress })
  .on('transactionHash', function(hash) {
    console.log(`Transaction hash: ${hash}`);
  })
  .on('confirmation', function(confirmationNumber, receipt) {
    console.log(`Confirmation number: ${confirmationNumber}`);
  })
  .on('error', function(error, receipt) {
    console.error(`Transaction error: ${error}`);
  });
