//go:generate protoc -I../proto ../proto/*.proto --go_out=. --go-grpc_out=.
package main

import (
	"context"
	"fmt"
	"grpc-go-python/client/generated/api"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
	"google.golang.org/grpc/grpclog"
)

func main() {
	cred := insecure.NewCredentials()
	client, err := grpc.NewClient(":11451", grpc.WithTransportCredentials(cred))
	if err != nil {
		grpclog.Fatalln(err.Error())
	}
	defer client.Close()

	helloService := api.NewHelloServiceClient(client)

	{
		resp, err := helloService.Hello(context.Background(), &api.HelloRequest{
			Name: "Cylix Lee",
		})
		if err != nil {
			grpclog.Fatalln(err.Error())
		}
		fmt.Println(resp)
	}

	{
		resp, err := helloService.Goodbye(context.Background(), &api.HelloRequest{
			Name: "李政翱",
		})
		if err != nil {
			grpclog.Fatalln(err.Error())
		}
		fmt.Println(resp)
	}
}
