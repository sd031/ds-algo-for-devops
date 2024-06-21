class Node {
    constructor(data) {
      this.data = data;
      this.prev = null;
      this.next = null;
    }
  }
  
  class CircularDoublyLinkedList {
    constructor() {
      this.head = null;
    }
  
    insertAtEnd(data) {
      const newNode = new Node(data);
      if (!this.head) {
        this.head = newNode;
        newNode.next = newNode;
        newNode.prev = newNode;
        return;
      }
      const last = this.head.prev;
      last.next = newNode;
      newNode.prev = last;
      newNode.next = this.head;
      this.head.prev = newNode;
    }
  
    insertAtBeginning(data) {
      const newNode = new Node(data);
      if (!this.head) {
        this.head = newNode;
        newNode.next = newNode;
        newNode.prev = newNode;
      } else {
        const last = this.head.prev;
        newNode.next = this.head;
        newNode.prev = last;
        this.head.prev = newNode;
        last.next = newNode;
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
      for (let i = 0; i < position; i++) {
        temp = temp.next;
        if (temp === this.head) {
          console.log("Position is greater than the length of the list.");
          return;
        }
      }
      newNode.next = temp;
      newNode.prev = temp.prev;
      temp.prev.next = newNode;
      temp.prev = newNode;
    }
  
    deleteNode(key) {
      if (!this.head) {
        return;
      }
      let temp = this.head;
      while (temp.data !== key) {
        temp = temp.next;
        if (temp === this.head) {
          return;
        }
      }
      if (temp.next === this.head && temp.prev === this.head) {
        this.head = null;
        return;
      }
      if (temp === this.head) {
        this.head = temp.next;
      }
      temp.prev.next = temp.next;
      temp.next.prev = temp.prev;
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
  const cdllist = new CircularDoublyLinkedList();
  cdllist.insertAtEnd(1);
  cdllist.insertAtEnd(2);
  cdllist.insertAtBeginning(0);
  cdllist.printList();  // Output: 0 1 2
  cdllist.deleteNode(1);
  cdllist.printList();  // Output: 0 2
  cdllist.insertAtPosition(1, 1);
  cdllist.printList();  // Output: 0 1 2
  