class Node {
    constructor(data) {
      this.data = data;
      this.next = null;
    }
  }
  
  class CircularLinkedList {
    constructor() {
      this.head = null;
    }
  
    insertAtEnd(data) {
      const newNode = new Node(data);
      if (!this.head) {
        this.head = newNode;
        newNode.next = this.head;
        return;
      }
      let temp = this.head;
      while (temp.next !== this.head) {
        temp = temp.next;
      }
      temp.next = newNode;
      newNode.next = this.head;
    }
  
    insertAtBeginning(data) {
      const newNode = new Node(data);
      if (!this.head) {
        this.head = newNode;
        newNode.next = newNode;
      } else {
        let temp = this.head;
        newNode.next = this.head;
        while (temp.next !== this.head) {
          temp = temp.next;
        }
        temp.next = newNode;
        this.head = newNode;
      }
    }
  
    insertAtPosition(position, data) {
      if (position < 0) {
        console.log("Position can't be negative.");
        return;
      }
      if (position === 0) {
        this.insertAtBeginning(data);
        return;
      }
      const newNode = new Node(data);
      let temp = this.head;
      for (let i = 0; i < position - 1; i++) {
        if (temp.next === this.head) {
          console.log("Position is greater than the length of the list.");
          return;
        }
        temp = temp.next;
      }
      newNode.next = temp.next;
      temp.next = newNode;
    }
  
    deleteNode(key) {
      if (!this.head) {
        return;
      }
      let temp = this.head;
      if (temp.data === key) {
        if (temp.next === this.head) {
          this.head = null;
        } else {
          while (temp.next !== this.head) {
            temp = temp.next;
          }
          temp.next = this.head.next;
          this.head = this.head.next;
        }
        return;
      }
      let prev = null;
      while (temp.next !== this.head && temp.data !== key) {
        prev = temp;
        temp = temp.next;
      }
      if (temp.data === key) {
        prev.next = temp.next;
      }
    }
  
    printList() {
      if (!this.head) {
        return;
      }
      let temp = this.head;
      do {
        process.stdout.write(temp.data + ' ');
        temp = temp.next;
      } while (temp !== this.head);
      console.log();
    }
  }
  
  // Usage
  const cllist = new CircularLinkedList();
  cllist.insertAtEnd(1);
  cllist.insertAtEnd(2);
  cllist.insertAtBeginning(0);
  cllist.printList();  // Output: 0 1 2
  cllist.deleteNode(1);
  cllist.printList();  // Output: 0 2
  cllist.insertAtPosition(1, 1);
  cllist.printList();  // Output: 0 1 2
  