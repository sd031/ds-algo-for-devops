class Node {
	constructor(data) {
	  this.data = data;
	  this.next = null;
	}
  }
  
  class LinkedList {
	constructor() {
	  this.head = null;
	}
  
	insertAtBeginning(data) {
	  const newNode = new Node(data);
	  newNode.next = this.head;
	  this.head = newNode;
	}
  
	insertAtEnd(data) {
	  const newNode = new Node(data);
	  if (!this.head) {
		this.head = newNode;
		return;
	  }
	  let last = this.head;
	  while (last.next) {
		last = last.next;
	  }
	  last.next = newNode;
	}
  
	insertAtPosition(position, data) {
	  if (position < 0) {
		console.log("Position can't be negative.");
		return;
	  }
	  const newNode = new Node(data);
	  if (position === 0) {
		newNode.next = this.head;
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
	  temp.next = newNode;
	}
  
	deleteNode(key) {
	  let temp = this.head;
	  if (temp && temp.data === key) {
		this.head = temp.next;
		temp = null;
		return;
	  }
	  let prev = null;
	  while (temp && temp.data !== key) {
		prev = temp;
		temp = temp.next;
	  }
	  if (!temp) {
		return;
	  }
	  prev.next = temp.next;
	  temp = null;
	}
  
	printList() {
	  let temp = this.head;
	  while (temp) {
		process.stdout.write(temp.data + ' ');
		temp = temp.next;
	  }
	  console.log();
	}
  }
  
  // Usage
  const llist = new LinkedList();
  llist.insertAtEnd(1);
  llist.insertAtEnd(2);
  llist.insertAtBeginning(0);
  llist.printList();  // Output: 0 1 2
  llist.deleteNode(1);
  llist.printList();  // Output: 0 2
  llist.insertAtPosition(1, 1);
  llist.printList();  // Output: 0 1 2
  