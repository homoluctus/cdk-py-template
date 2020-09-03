# cdk-py-template

AWS CDK Python Template

<!-- TOC depthFrom:2 -->

- [Requirements](#requirements)
- [Setup](#setup)
  - [1. Install aws-cdk](#1-install-aws-cdk)
  - [2. Install Python dependencies](#2-install-python-dependencies)
- [Directory](#directory)

<!-- /TOC -->

## Requirements

- Python ^3.8
- pipenv
- yarn / npm

## Setup

### 1. Install aws-cdk

```bash
yarn global add aws-cdk
```

OR

```bash
npm i -g aws-cdk
```

### 2. Install Python dependencies

```bash
pipenv sync -d
```

## Directory

```
.
├── app.py
├── cdk.json
└── src
     ├── __init__.py
     ├── entity
     ├── props
     └── stack
```
