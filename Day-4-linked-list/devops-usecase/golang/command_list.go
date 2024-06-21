package main

import (
	"bytes"
	"fmt"
	"os/exec"
	"strings"
)

type CommandNode struct {
	command string
	status  *bool // nil: not executed, true: success, false: failure
	output  string
	error   string
	prev    *CommandNode
	next    *CommandNode
}

type CommandList struct {
	head *CommandNode
}

func NewCommandList() *CommandList {
	return &CommandList{}
}

func (cl *CommandList) AddCommand(command string) {
	newNode := &CommandNode{command: command}
	if cl.head == nil {
		cl.head = newNode
	} else {
		temp := cl.head
		for temp.next != nil {
			temp = temp.next
		}
		temp.next = newNode
		newNode.prev = temp
	}
}

func (cl *CommandList) ExecuteCommands() {
	temp := cl.head
	for temp != nil {
		cmd := exec.Command("sh", "-c", temp.command)
		var out bytes.Buffer
		var stderr bytes.Buffer
		cmd.Stdout = &out
		cmd.Stderr = &stderr
		err := cmd.Run()
		if err != nil {
			status := false
			temp.status = &status
			temp.error = stderr.String()
			fmt.Printf("Command '%s' failed with error: %s\n", temp.command, temp.error)
		} else {
			status := true
			temp.status = &status
			temp.output = out.String()
			fmt.Printf("Command '%s' succeeded.\n", temp.command)
		}
		temp = temp.next
	}
}

func (cl *CommandList) PrintCommandsStatus() {
	temp := cl.head
	for temp != nil {
		status := "Not Executed"
		if temp.status != nil {
			if *temp.status {
				status = "Success"
			} else {
				status = "Failure"
			}
		}
		fmt.Printf("Command: %s, Status: %s\n", temp.command, status)
		if temp.output != "" {
			fmt.Printf("Output: %s\n", strings.TrimSpace(temp.output))
		}
		if temp.error != "" {
			fmt.Printf("Error: %s\n", strings.TrimSpace(temp.error))
		}
		fmt.Println()
		temp = temp.next
	}
}

func (cl *CommandList) PrintCommandsForward() {
	temp := cl.head
	for temp != nil {
		fmt.Print(temp.command)
		if temp.next != nil {
			fmt.Print(" <-> ")
		}
		temp = temp.next
	}
	fmt.Println()
}

func (cl *CommandList) PrintCommandsBackward() {
	temp := cl.head
	if temp == nil {
		return
	}
	for temp.next != nil {
		temp = temp.next
	}
	for temp != nil {
		fmt.Print(temp.command)
		if temp.prev != nil {
			fmt.Print(" <-> ")
		}
		temp = temp.prev
	}
	fmt.Println()
}

func main() {
	cmdList := NewCommandList()
	cmdList.AddCommand("echo 'Hello World'")
	cmdList.AddCommand("ls -l")
	cmdList.AddCommand("invalid_command") // This will simulate a failed command
	cmdList.AddCommand("pwd")

	fmt.Println("Commands in order (Forward):")
	cmdList.PrintCommandsForward()

	fmt.Println("\nExecuting commands...")
	cmdList.ExecuteCommands()

	fmt.Println("\nCommands status:")
	cmdList.PrintCommandsStatus()

	fmt.Println("\nCommands in order (Backward):")
	cmdList.PrintCommandsBackward()
}
