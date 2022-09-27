package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"log"
	"net/http"
)

func main() {
	router := gin.Default()
	router.LoadHTMLFiles("my_blog/upload.html")
	router.MaxMultipartMemory = 64 << 20 // 64 MB

	router.POST("/upload", func(c *gin.Context) {
		// file是表单字段名字
		file, _ := c.FormFile("file")
		// 打印上传的名字
		log.Println(file.Filename)

		//将上传的文件保存到./data/shirdon.jpg文件中
		c.SaveUploadedFile(file, "./data/shirdon.jpg")
		c.String(http.StatusOK, fmt.Sprintf("'%s' upload", file.Filename))
	})
	router.Run(":8080")
}
