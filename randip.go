//Testing port fot Golang

package main

import (
	"fmt"
	"math/rand"
	"time"
	"strings"
	"net"
	"runtime"
	"sync"
	"io/ioutil"
)

var IP = ""

var num = 0

var IPsucc [100]string = [100]string{}

func aToS(a [4]int, delim string) string {
	return strings.Trim(strings.Replace(fmt.Sprint(a), " ", delim, -1), "[]")
}

func genIP() {
	var IPaddr [4]int
	i := 0
	for i != 4 {
		s1 := rand.NewSource(time.Now().UnixNano())
		r1 := rand.New(s1)
		IPaddr[i] = r1.Intn(255)
		i += 1
	}
IP = aToS(IPaddr, ".")
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func paraConn() {
        x := 0
        for x != 1 {
                genIP()
                fmt.Println("Attempting connection on " + IP)
                IPconn := (IP + ":80")
                timeout := time.Duration(5) * time.Second
                conn, err := net.DialTimeout("tcp", IPconn , timeout)
                if err != nil {
                        fmt.Println(err)
                        fmt.Println("")
                        continue
                } else {
                        defer conn.Close()
                        fmt.Println(IP + ": Connected")
                        fmt.Println("")
			IPfile := []byte(IP + "\n")
			frr := ioutil.WriteFile("IP.txt", IPfile, 0644)
			check(frr)
                        continue
                }
        }
}


func main() {

	runtime.GOMAXPROCS(1)
	var wg sync.WaitGroup
	wg.Add(4)

	fmt.Println("Starting Go Procs...")
	fmt.Println("")

	//proc1
	go func() {
		defer wg.Done()
		paraConn()
	}()
	//proc2
	go func() {
		defer wg.Done()
		paraConn()
	}()
	//proc3
	go func() {
		defer wg.Done()
		paraConn()
	}()
	//proc4
	go func() {
		defer wg.Done()
		paraConn()
	}()
	wg.Wait()

}
