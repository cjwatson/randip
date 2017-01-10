//Testing port fot Golang

package main

import (
        "fmt"
        "math/rand"
        "time"
        "strings"
        "net"
)

var IP = ""

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

func main() {
        x := 0
        for x != 10 {
                genIP()
                fmt.Println("Attempting connection on " + IP)
                IPconn := (IP + ":80")
                timeout := time.Duration(5) * time.Second
                conn, err := net.DialTimeout("tcp", IPconn , timeout)
                if err != nil {
                        fmt.Println(err)
                        fmt.Println("")
                        x += 1
                        continue
                } else {
                        defer conn.Close()
                        fmt.Println(IP + ": Connected")
                        fmt.Println("")
                        x += 1
                        continue
                }
        }
}
