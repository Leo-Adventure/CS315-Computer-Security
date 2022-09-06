# CTF Track Week 1

## SID: 12012919

## Name：廖铭骞

### Q1

Since the flag can be fetched in the QQ group, the flag is 

`w3Lc0Me_T0_cS315!`

### Q2

The flag is `17uaji1l`

I obtained the flag by the following steps:

1. open the `pcapng` file in wireshark
2. filter out all the HTTP packets
3. find the packets with info like"HTTP/1.1 206 Partial Content (text plain)"
4. extract the flag information by examining all the corresponding packets.
