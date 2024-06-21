class Node {
    constructor(data) {
      this.data = data;
      this.prev = null;
      this.next = null;
    }
  }
  
  class DoublyLinkedList {
    constructor() {
      this.head = null;
    }
  
    insertAtBeginning(data) {
      const newNode = new Node(data);
      newNode.next = this.head;
      if (this.head !== null) {
        this.head.prev = newNode;
      }
      this.head = newNode;
    }
  
    insertAtEnd(data) {
      const newNode = new Node(data);
      if (this.head === null) {
        this.head = newNode;
        return;
      }
      let last = this.head;
      while (last.next) {
        last = last.next;
      }
      last.next = newNode;
      newNode.prev = last;
    }
  
    insertAtPosition(position, data) {
      if (position < 0) {
        console.log("Position can't be negative.");
        return;
      }
      const newNode = new Node(data);
      if (position === 0) {
        newNode.next = this.head;
        if (this.head !== null) {
          this.head.prev = newNode;
        }
        this.head = newNode;
        return;
      }
      let temp = this.head;
      for (let i = 0; i < position - 1; i++) {
        if (!temp) {
          console.log("Position is greater than the length of the list.");
          return;
        }
        temp = temp.next;
      }
      if (!temp) {
        console.log("Position is greater than the length of the list.");
        return;
      }
      newNode.next = temp.next;
      newNode.prev = temp;
      if (temp.next !== null) {
        temp.next.prev = newNode;
      }
      temp.next = newNode;
    }
  
    deleteNode(key) {
      let temp = this.head;
      if (temp !== null && temp.data === key) {
        this.head = temp.next;
        if (this.head !== null) {
          this.head.prev = null;
        }
        temp = null;
        return;
      }
      while (temp !== null && temp.data !== key) {
        temp = temp.next;
      }
      if (temp === null) {
        return;
      }
      if (temp.next !== null) {
        temp.next.prev = temp.prev;
      }
      if (temp.prev !== null) {
        temp.prev.next = temp.next;
      }
      temp = null;
    }
  
    printListForward() {
      let temp = this.head;
      while (temp) {
        process.stdout.write(temp.data + ' ');
        temp = temp.next;
      }
      console.log();
    }
  
    printListBackward() {
      let temp = this.head;
      if (!temp) return;
      while (temp.next) {
        temp = temp.next;
      }
      while (temp) {
        process.stdout.write(temp.data + ' ');
        temp = temp.prev;
      }
      console.log();
    }
  }
  
  // Usage
  const dllist = new DoublyLinkedList();
  dllist.insertAtEnd(1);
  dllist.insertAtEnd(2);
  dllist.insertAtBeginning(0);
  dllist.printListForward();  // Output: 0 1 2
  dllist.printListBackward(); // Output: 2 1 0
  dllist.deleteNode(1);
  dllist.printListForward();  // Output: 0 2
  dllist.insertAtPosition(1, 1);
  dllist.printListForward();  // Output: 0 1 2
  dllist.printListBackward(); // Output: 2 1 0
  