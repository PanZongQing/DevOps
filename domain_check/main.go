package main

import (
	"fmt"
	"os"

	"github.com/monochromegane/go-whois"
)

func main() {
	res, err := whois.Query(os.Args[1])
	if err != nil {
		fmt.Println(err)
	}
	res.Raw()   // get original WHOIS response.
	res.Exist() // check domain exist.
}
