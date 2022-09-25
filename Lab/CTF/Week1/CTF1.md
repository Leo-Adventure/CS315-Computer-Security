# Assignment 1

## SID：12012919

## Name: 廖铭骞

## 题目1  Sign in

题目描述：What's a CTF? Join our QQ Group to get the flag!

### 分析

We can follow the steps 

### 步骤

1. Join the QQ group
2. Open the group announcement

### Flag

`flag{w3Lc0Me_T0_cS315!}`

## 题目2  HTTP code 206

题目描述：Flag? Flag!

### 分析

We can follow the steps 

### 步骤

1. open the `pcapng` file in wireshark
2. filter out all the HTTP packets
3. find the packets with info like"HTTP/1.1 206 Partial Content (text plain)"
4. extract the flag information by examining all the corresponding packets.

### Flag

`flag{17uaji1l}`

## 题目3 Time-based SQL Injection

题目描述：In fact this isn't a Web challenge.

### 分析

We can follow the steps 

### 步骤

1. open the `pcapng` file in wireshark
2. filter out all the packets that contains the string `sleep%25283%2529`
3. convert all the `%` to meaningful characters according to the HTTP Escape character table
4. find the max number of each group that is divides by their indexes
5. then convert all the max numbers to the characters corresponding.
6. combine all the characters.
7. get the flag

### Flag

` flag{1qwy2781}`

