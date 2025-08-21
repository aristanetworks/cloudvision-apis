// Copyright (c) 2025 Arista Networks, Inc.  All rights reserved.
// Arista Networks, Inc. Confidential and Proprietary.
// Subject to Arista Networks, Inc.'s EULA.
// FOR INTERNAL USE ONLY. NOT FOR DISTRIBUTION.

package main

import (
	"flag"
	"log"
	"os"
	"sort"
	"strings"
	"text/template"
)

const modelsTemplate = `---
title: "Models"
---

Models are also listed under the sidebar tab ` + "`Models`" + `

{{range .}}
- [{{.}}](/cloudvision-apis/models/{{.}}/){{end}}
`

// main function is to generate a markdown file that contains links to all the resources
func main() {
	outputFile := flag.String("out", "", "Output markdown file")
	protoDirs := flag.String("protodirs", "", "Space separated list of proto directories")
	flag.Parse()

	if *outputFile == "" {
		log.Fatal("Error: -out (output markdown file) must be specified")
	}
	if *protoDirs == "" {
		log.Fatal("Error: -protodirs must be specified")
	}

	dirs := strings.Split(*protoDirs, " ")
	sort.Strings(dirs)

	t, err := template.New("models").Parse(modelsTemplate)
	if err != nil {
		log.Fatalf("failed to parse models template: %v", err)
	}

	output, err := os.Create(*outputFile)
	if err != nil {
		log.Fatalf("failed to create output markdown file %s: %v", *outputFile, err)
	}
	defer output.Close()

	err = t.Execute(output, dirs)
	if err != nil {
		log.Fatalf("failed to execute template: %v", err)
	}
}
