# Information_Security_encryption-decryption-algorithms

Cryptography at its very core is math. Pure, simple, undiluted math. Math created the algorithms that are the basis for all encryption. And encryption is the basis for privacy and security on the internet. So, we love math. Even if it is a tad complicated. With that being said, algorithms have to be built to work against computers. As computers get smarter, algorithms become weaker and we must therefore look at new solutions. This is how cryptography evolves to beat the bad guys.

So how is it done? First you need to build a cryptosystem that is both confidential and authentic. This cryptosystem is responsible for creating the key(s) that will be used to encrypt and then decrypt the data or message. A number of signing algorithms have been created over the years to create these keys, some of which have since been deprecated as computing power has increased. 


Brute Force Attack

A brute force attack or a dictionary attack as it’s also known is a trial and error method of obtaining the private key of an encrypted packet of data. The trial and error is done by a computer so the higher the computational power, the more “tries” it can have in a short space of time. As computing power and performance increases, the ability to find the private key increases, unless you increase the length of the key so that a higher number of possibilities exist.


Encryption Key Sizes

Key size or key length refers to the number of bits in a key used by a cryptographic algorithm. Only the correct key can decrypt a ciphertext (output) back into plaintext (input). As CPU power gets more advanced, the computational time required to brute force an encryption key gets less and less. As such, keys have had to become longer. For many years the limit was 40-bits, but today we are seeing up to 4096-bit key lengths in cryptography.

Block Sizes

Some algorithms use “block ciphers”, which encrypt and decrypt data in blocks (fixed length groups of bits). There is a relationship between block size and the amount of data that can be encrypted without duplicating blocks, the explanation of which is beyond the scope of this post, but the key takeaway is that the current recommendation is to use at least 128 bit blocks.   

Symmetric Key Algorithms
symmetric algorithms

A symmetric key algorithm (also known as a secret key algorithm), uses the concept of a key and lock to encrypt plaintext and decrypt ciphertext data. The same “key” is used to both encrypt and decrypt the file. They are sub-classified by stream ciphers and block ciphers. A stream cipher is where plaintext digits are combined with a pseudo-random cipher digit stream. Block ciphers take the number of bits and encrypt them as a single unit (known as rounds), padding the plaintext so that it’s a multiple of a block size.

The algorithm itself is not kept a secret and the sender and receiver of communication must both have copies of the secret key in a secure place. The use of the same key is also one of the drawbacks of symmetric key cryptography because if someone can get hold of the key, they can decrypt your data.

DES
The Data Encryption Standard or DES was, and probably still is, one of the more well-known algorithms of the modern cryptographic era. Today it is widely considered insecure. DES was developed in the 1970’s by IBM and was later submitted to the National Bureau of Standards (NBS) and National Security Agency (NSA). The involvement of the NSA in the design sparked controversial rumours of backdoors, creating widespread scrutiny. It wasn’t until 1976 that DES was approved as a cryptographic standard and published in FIPS.

In the 1990’s, computing 72 quadrillion possible keys for a 56 bit DES key seemed highly improbable. This would have been true for one computer, but in 1997 a group of computer scientists led by Rocke Verser used thousands of volunteer computers to crack DES within 24 hours, thereby making him and his team the winner of the $10,000 DES Challenge.

Since then, DES was fortified with new updates called double-DES and triple-DES, simply layering the cipher so that it would have to decrypt three times to each data block. Triple-DES is still used in some places, but AES (see below) has become the new standard since then.

In Use Today? – DES and double-DES are no longer in use, but triple-DES with three keys is still a recommended algorithm in NIST SP 800-57. It is much slower to use than the AES algorithm, but is still seen in the electronic payment industry. It is also used in Microsoft OneNote and Outlook 2007 to protect user content and system data and the browsers Firefox and Mozilla Thunderbird in CBC mode to encrypt website authentication login credentials when using a master password.

AES
The Advanced Encryption Standard or AES was established by the National Institute of Standards and Technology (NIST) in 2001. AES has been adopted by the US government with key lengths of 128, 192 and 256 bits.

AES has a fairly simple mathematical framework that some argue makes it susceptible to attack. The theoretical XSL attack was announced in 2002 and since then security researchers such as Bruce Schneier have found ways to exploit parts of the algorithm. However, it is important to note that even in Bruce Schneier’s article, he states that there is no reason to panic just yet since they only break 11 of the full 14 rounds of AES-256, taking 270 time. It also requires the cryptographer to have access to plaintexts encrypted with related multiple keys, which still gives AES a higher safety margin but just not as high as previously thought.

In Use Today? – Yes! AES is still in wide use today for its better processing power and ability to be used in a wide range of hardware like smart cards and high-performance computers.


Diffie-Hellman
Diffie-Hellman is one of the first recorded examples of asymmetric cryptography, first conceptualized by Ralph Merkle and put into fruition by Whitfield Diffie and Martin Hellman. Traditionally, secure encrypted communication would require both parties to first exchange their keys by some secure physical channel. Diffie-Hellman eliminated the need for the secure exchange by creating an additional key, the public key.

At this moment in time, Deffie-Hellman is no longer the standard cryptographic algorithm because it has been found to be vulnerable to several attacks. A Logjam attack, for example, can allow man-in-the-middle attacks where the hacker can read and modify any data sent over the connection.

In Use Today? – Yes. For general PKI security and digital signing, NIST recommends RSA (see below) because Diffie-Hellman requires more CPU power and larger data exchange for Digital Signing and SSL in particular. But there are still some uses of Diffie-Hellman in the public sphere today for example, in Elliptic Curve Cryptography.

RSA
The Rivest-Shammir-Adleman algorithm, better known as RSA, is now the most widely used asymmetric cryptosystem on the web today. RSA is based on the factorization of prime numbers, because working backwards from two multiplied prime numbers is computationally difficult to do, more so as the prime numbers get larger. The challenge of breaking RSA is known as the ‘RSA problem’.

RSA is a slow algorithm and because of this, it is used to encrypt and decrypt the symmetric keys which in turn, encrypt and decrypt the communications. The symmetric keys perform the bulk of the work, while RSA creates a strong and secure channel.

In 1998, Daniel Bleichenbacher described how he exploited a vulnerability in the PKCS#1 file (used to carry the private key). His attack was able to retrieve the private key and use it to recover session keys and decrypt messages. As a result of his work, RSA Laboratories released new versions of PKCS#1 that are not vulnerable to the same attack. While some attacks to RSA have been attempted, the algorithm remains strong, arguably until quantum computers become mainstream.

In Use Today? – Yes. RSA is the most widely used asymmetric algorithm today.

