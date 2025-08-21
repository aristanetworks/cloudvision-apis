// Copyright (c) 2025 Arista Networks, Inc.  All rights reserved.
// Arista Networks, Inc. Confidential and Proprietary.
// Subject to Arista Networks, Inc.'s EULA.
// FOR INTERNAL USE ONLY. NOT FOR DISTRIBUTION.

package main

import (
	"bytes"
	"flag"
	"fmt"
	"log"
	"os"
	"os/exec"
	"path/filepath"
	"sort"
	"strings"
	"text/template"

	"github.com/Masterminds/semver/v3"
	"gopkg.in/yaml.v3"
)

type Change struct {
	Date        string `yaml:"date"`
	Description string `yaml:"description"`
	Version     string `yaml:"version"`
	Onprem      bool   `yaml:"onprem"`
	Cvaas       bool   `yaml:"cvaas"`
}

type Changelog struct {
	Changes []Change `yaml:"Changes"`
}

type MarkdownTemplateData struct {
	Title   string
	Version string
	Body    string
}

func extractVersions(filePath string) ([]*semver.Version, error) {
	file, err := os.Open(filePath)
	if err != nil {
		return nil, fmt.Errorf("failed to open changelog file %s: %w", filePath, err)
	}
	defer file.Close()

	var changelog Changelog
	decoder := yaml.NewDecoder(file)
	if err := decoder.Decode(&changelog); err != nil {
		return nil, fmt.Errorf("failed to decode YAML file %s: %w", filePath, err)
	}

	var versions []*semver.Version
	for _, change := range changelog.Changes {
		if change.Version != "" {
			semVer, err := semver.NewVersion(change.Version)
			if err != nil {
				continue
			}
			versions = append(versions, semVer)
		}
	}
	return versions, nil
}

func getVersionForProto(repoRoot, protoPath string) (string, error) {
	resourceDir := filepath.Dir(protoPath)

	resourceName := filepath.Base(resourceDir)
	resourceName = strings.TrimSuffix(resourceName, filepath.Ext(resourceName))

	changelogPath := filepath.Join(resourceDir, resourceName+"-changelog.yaml")

	versions, err := extractVersions(changelogPath)
	if err != nil {
		return "", fmt.Errorf("failed to extract versions from %s: %w", changelogPath, err)
	}

	if len(versions) == 0 {
		return "unknown", nil
	}

	sort.Sort(semver.Collection(versions))
	return versions[len(versions)-1].String(), nil
}

func generateMarkdown(inputFile, outputFile, repoRoot string, version string) error {
	// Use protoc to generate the full markdown content
	cmd := exec.Command("protoc",
		"-I", repoRoot,
		"--doc_out=.",
		"--doc_opt=model.tmpl,output.tmp",
		inputFile,
		filepath.Join(filepath.Dir(inputFile), "services.gen.proto"),
	)

	var out bytes.Buffer
	cmd.Stdout = &out
	cmd.Stderr = os.Stderr

	if err := cmd.Run(); err != nil {
		return fmt.Errorf("failed to run protoc command: %w", err)
	}

	body, err := os.ReadFile("output.tmp")
	if err != nil {
		return fmt.Errorf("failed to read generated markdown: %w", err)
	}
	if err := os.Remove("output.tmp"); err != nil {
		return fmt.Errorf("failed to remove temporary file output.tmp: %w", err)
	}

	fullTmpl := `---
title: {{.Title}}
version: {{.Version}}
---

import ShowVersion from '@site/src/components/ShowVersion';

<ShowVersion version="{{.Version}}" />

{{.Body}}
`
	t, err := template.New("markdown").Parse(fullTmpl)
	if err != nil {
		return fmt.Errorf("failed to parse markdown template: %w", err)
	}

	output, err := os.Create(outputFile)
	if err != nil {
		return fmt.Errorf("failed to create output markdown file %s: %w", outputFile, err)
	}
	defer output.Close()

	sanitized := strings.ReplaceAll(string(body), "<->", "\\<-\\>")

	return t.Execute(output, MarkdownTemplateData{
		Title:   filepath.Base(filepath.Dir(inputFile)),
		Version: version,
		Body:    sanitized,
	})
}

// main function is to generate markdown files for each released resource.
func main() {
	repoRoot := flag.String("root", "../", "Path to repository root")
	inputFile := flag.String("in", "", "Input proto file")
	outputFile := flag.String("out", "", "Output markdown file")
	flag.Parse()

	if *inputFile == "" {
		log.Fatal("Error: -in (input proto file) must be specified")
	}
	if *outputFile == "" {
		log.Fatal("Error: -out (output markdown file) must be specified")
	}

	version, err := getVersionForProto(*repoRoot, *inputFile)
	if err != nil {
		log.Fatalf("Failed to get version: %v", err)
	}

	err = generateMarkdown(*inputFile, *outputFile, *repoRoot, version)
	if err != nil {
		log.Fatalf("Failed to generate markdown: %v", err)
	}
}
