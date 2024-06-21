const { exec } = require('child_process');

class CommandNode {
  constructor(command) {
    this.command = command;
    this.status = null; // null: not executed, true: success, false: failure
    this.output = null;
    this.error = null;
    this.prev = null;
    this.next = null;
  }
}

class CommandList {
  constructor() {
    this.head = null;
  }

  addCommand(command) {
    const newNode = new CommandNode(command);
    if (!this.head) {
      this.head = newNode;
    } else {
      let temp = this.head;
      while (temp.next) {
        temp = temp.next;
      }
      temp.next = newNode;
      newNode.prev = temp;
    }
  }

  async executeCommands() {
    let temp = this.head;
    while (temp) {
      try {
        const result = await this.runCommand(temp.command);
        temp.status = true;
        temp.output = result.stdout;
        temp.error = result.stderr;
        console.log(`Command '${temp.command}' succeeded.`);
      } catch (error) {
        temp.status = false;
        temp.output = error.stdout;
        temp.error = error.stderr;
        console.log(`Command '${temp.command}' failed with error: ${error.stderr.trim()}`);
      }
      temp = temp.next;
    }
  }

  runCommand(command) {
    return new Promise((resolve, reject) => {
      exec(command, (error, stdout, stderr) => {
        if (error) {
          reject({ stdout, stderr });
        } else {
          resolve({ stdout, stderr });
        }
      });
    });
  }

  printCommandsStatus() {
    let temp = this.head;
    while (temp) {
      const status = temp.status === null ? "Not Executed" : temp.status ? "Success" : "Failure";
      console.log(`Command: ${temp.command}, Status: ${status}`);
      if (temp.output) {
        console.log(`Output: ${temp.output.trim()}`);
      }
      if (temp.error) {
        console.log(`Error: ${temp.error.trim()}`);
      }
      console.log();
      temp = temp.next;
    }
  }

  printCommandsForward() {
    let temp = this.head;
    while (temp) {
      process.stdout.write(temp.command);
      if (temp.next) {
        process.stdout.write(' <-> ');
      }
      temp = temp.next;
    }
    console.log();
  }

  printCommandsBackward() {
    let temp = this.head;
    if (!temp) return;
    while (temp.next) {
      temp = temp.next;
    }
    while (temp) {
      process.stdout.write(temp.command);
      if (temp.prev) {
        process.stdout.write(' <-> ');
      }
      temp = temp.prev;
    }
    console.log();
  }
}

// Usage
const cmdList = new CommandList();
cmdList.addCommand("echo 'Hello World'");
cmdList.addCommand("ls -l");
cmdList.addCommand("invalid_command"); // This will simulate a failed command
cmdList.addCommand("pwd");

console.log("Commands in order (Forward):");
cmdList.printCommandsForward();

console.log("\nExecuting commands...");
cmdList.executeCommands().then(() => {
  console.log("\nCommands status:");
  cmdList.printCommandsStatus();

  console.log("\nCommands in order (Backward):");
  cmdList.printCommandsBackward();
});
