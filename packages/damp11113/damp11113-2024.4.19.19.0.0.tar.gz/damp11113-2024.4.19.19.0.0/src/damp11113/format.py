"""
damp11113-library - A Utils library and Easy to use. For more info visit https://github.com/damp11113/damp11113-library/wiki
Copyright (C) 2021-2023 damp11113 (MIT)

Visit https://github.com/damp11113/damp11113-library

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import struct
import zlib
import bitarray
import random

# multiplex4 (m4) format
def create_multiplex4_file(filename, sample_rate, data_format, data_streams):
    with open(filename, 'wb') as file:
        # Write header information
        header = struct.pack('!If', sample_rate, data_format)
        file.write(header)

        # Write data streams
        for stream_data in data_streams:
            metadata = struct.pack('!I', stream_data['id'])  # Example: Stream ID
            file.write(metadata)

            # Write IQ data for each stream
            for iq_sample in stream_data['iq_data']:
                iq_byte = struct.pack('!B', iq_sample)  # Pack the 4-bit IQ sample into a byte
                file.write(iq_byte)

def read_multiplex4_file(file_path):
    with open(file_path, 'rb') as file:
        # Read header information
        header = file.read(8)  # Assuming header is 8 bytes long (4 bytes for sample rate, 4 bytes for format)
        sample_rate, data_format = struct.unpack('!If', header)

        data_streams = []

        # Read data streams
        while True:
            metadata = file.read(4)  # Assuming metadata is 4 bytes long (e.g., stream ID)
            if not metadata:
                break  # Reached the end of the file

            stream_id = struct.unpack('!I', metadata)[0]  # Extract the stream ID

            iq_data = []
            while True:
                iq_byte = file.read(1)  # Assuming each IQ sample is represented by 1 byte (8 bits)
                if not iq_byte:
                    break  # Reached the end of the current data stream

                iq_sample = struct.unpack('!B', iq_byte)[0]  # Unpack the byte as a single 4-bit IQ sample
                iq_data.append(iq_sample)

            data_streams.append({'id': stream_id, 'iq_data': iq_data})

    for stream_data in data_streams:
        iq = '|'.join([str(num) for num in stream_data['iq_data']])
    iqlist = iq.split("|0|0|0")
    iqdi = []
    for id, iqidremove in enumerate(iqlist):
        if id == 0:
            iqdi.append(iqidremove)
        else:
            iqdi.append(iqidremove[3:])
    iqdi2 = []
    for iqreplace in iqdi:
        iqdi2.append(iqreplace.replace('|', ','))
    iqpr = [list(map(int, item.split(','))) for item in iqdi2]
    data_streams = []
    for id, iq in enumerate(iqpr):
        data_streams.append({
            'id': id,
            'iq_data': iq
        })

    return sample_rate, data_format, data_streams

#--------------------------------------------------------------------------------------------------------------

class BrainfuckInterpreter:
    def __init__(self):
        self.memory = [0] * 30000
        self.pointer = 0
        self.output = ""

    def interpret(self, code):
        loop_stack = []
        code_pointer = 0

        while code_pointer < len(code):
            command = code[code_pointer]

            if command == '>':
                self.pointer += 1
            elif command == '<':
                self.pointer -= 1
            elif command == '+':
                self.memory[self.pointer] = (self.memory[self.pointer] + 1) % 256
            elif command == '-':
                self.memory[self.pointer] = (self.memory[self.pointer] - 1) % 256
            elif command == '.':
                self.output += chr(self.memory[self.pointer])
            elif command == ',':
                # Input operation is not implemented in this basic interpreter
                pass
            elif command == '[':
                if self.memory[self.pointer] == 0:
                    loop_depth = 1
                    while loop_depth > 0:
                        code_pointer += 1
                        if code[code_pointer] == '[':
                            loop_depth += 1
                        elif code[code_pointer] == ']':
                            loop_depth -= 1
                else:
                    loop_stack.append(code_pointer)
            elif command == ']':
                if self.memory[self.pointer] != 0:
                    code_pointer = loop_stack[-1] - 1
                else:
                    loop_stack.pop()
            code_pointer += 1

        return self.output

#------------------------------------------------------------------------------------------------------

class RangeEncoder(object):
    def __init__(self, encoding, bits=32):
        """If encoding=True, initialize and support encoding operations. Otherwise,
        support decoding operations. More state bits will give better encoding
        accuracy at the cost of speed."""
        assert encoding in (True, False)
        assert bits > 0
        self.encoding = encoding
        self.finished = False
        # Range state.
        self.bits = bits
        self.norm = 1 << bits
        self.half = self.norm >> 1
        self.low = 0
        self.range = self.norm if encoding else 1
        # Bit queue for data we're ready to input or output.
        qmask = (bits * 4 - 1) | 8
        while qmask & (qmask + 1):
            qmask |= qmask >> 1
        self.qmask = qmask
        self.qcount = [0] * (qmask + 1)
        self.qlen = 0
        self.qpos = 0

    def encode(self, intlow, inthigh, intden):
        """Encode an interval into the range."""
        assert self.encoding and not self.finished
        assert 0 <= intlow < inthigh <= intden <= self.half + 1
        assert self.qlen <= (self.qmask >> 1)
        qmask = self.qmask
        qcount = self.qcount
        qpos = self.qpos
        qlen = self.qlen
        # Shift the range.
        half = self.half
        low = self.low
        range_val = self.range
        while range_val <= half:
            # Push a settled state bit the to queue.
            dif = qpos ^ ((low & half) != 0)
            qpos = (qpos + (dif & 1)) & qmask
            qlen += qcount[qpos] == 0
            qcount[qpos] += 1
            low += low
            range_val += range_val
        norm = self.norm
        low &= norm - 1
        # Scale the range to fit in the interval.
        off = (range_val * intlow) // intden
        low += off
        range_val = (range_val * inthigh) // intden - off
        # If we need to carry.
        if low >= norm:
            # Propagate a carry up our queue. If the previous bits were 0's, flip one to 1.
            # Otherwise, flip all 1's to 0's.
            low -= norm
            # If we're on an odd parity, align us with an even parity.
            odd = qpos & 1
            ones = qcount[qpos] & -odd
            qcount[qpos] -= ones
            qpos -= odd
            # Even parity carry operation.
            qcount[qpos] -= 1
            inc = 1 if qcount[qpos] else -1
            qpos = (qpos + inc) & qmask
            qcount[qpos] += 1
            # Length correction.
            qlen += inc
            qlen += qlen <= odd
            # If we were on an odd parity, add in the 1's-turned-0's.
            qpos = (qpos + odd) & qmask
            qcount[qpos] += ones
        self.low = low
        self.range = range_val
        self.qpos = qpos
        self.qlen = qlen

    def finish(self):
        """Flush the remaining data from the range."""
        if self.finished:
            return
        self.finished = True
        if not self.encoding:
            # We have no more data to decode. Pad the queue with 1's from now on.
            return
        assert self.qlen <= (self.qmask >> 1)
        # We have no more data to encode. Flush out the minimum number of bits necessary
        # to satisfy low <= flush+1's < low+range. Then pad with 1's till we're byte aligned.
        qmask = self.qmask
        qcount = self.qcount
        qpos = self.qpos
        qlen = self.qlen
        low = self.low
        norm = self.norm
        dif = low ^ (low + self.range)
        while dif < norm:
            low += low
            dif += dif
            flip = qpos ^ ((low & norm) != 0)
            qpos = (qpos + (flip & 1)) & qmask
            qlen += qcount[qpos] == 0
            qcount[qpos] += 1
        # Calculate how many bits need to be appended to be byte aligned.
        pad = sum(qcount[(qpos - i) & qmask] for i in range(qlen)) % 8
        # If we're not byte aligned.
        if pad != 0:
            # Align us with an odd parity and add the pad. Add 1 to qlen if qpos & 1 = 0.
            qlen -= qpos
            qpos |= 1
            qlen += qpos
            qcount[qpos] += 8 - pad
        self.qpos = qpos
        self.qlen = qlen

    def hasbyte(self):
        """Is a byte ready to be output?"""
        return self.qlen >= 10 or (self.finished and self.qlen)

    def getbyte(self):
        """If data is ready to be output, returns a bytes object. Otherwise, returns None."""
        assert self.encoding
        qlen = self.qlen
        if qlen < 8 and (not self.finished or qlen == 0):
            return None
        # Go back from the end of the queue and shift bits into ret.
        # If we use all bits at a position, advance the position.
        qmask = self.qmask
        orig = self.qpos + 1
        qpos = orig - qlen
        qcount = self.qcount
        ret = 0
        for i in range(8):
            ret = (ret << 1) | (qpos & 1)
            pos = qpos & qmask
            qcount[pos] -= 1
            qpos += qcount[pos] == 0
        self.qlen = orig - qpos
        return bytes([ret])

    def decode(self, intden):
        """Given an interval denominator, find a value in [0,intden) that will fall
        into some interval. Returns None if more data is needed."""
        assert not self.encoding
        assert intden <= self.half + 1
        qmask = self.qmask
        qpos = self.qpos
        qlen = (self.qlen - qpos) & qmask
        qcount = self.qcount
        if qlen < self.bits:
            # If the input has not signaled it is finished, request more bits.
            if not self.finished:
                return None
            # If we are reading from a finished stream, pad the entire queue with 1's.
            qlen = self.qlen
            while True:
                qcount[qlen] = 1
                qlen = (qlen + 1) & qmask
                if qlen == qpos:
                    break
            self.qlen = (qpos - 1) & qmask
        # Shift the range.
        half = self.half
        low = self.low
        range_val = self.range
        while range_val <= half:
            low += low + qcount[qpos]
            qpos = (qpos + 1) & qmask
            range_val += range_val
        self.qpos = qpos
        self.low = low
        self.range = range_val
        # Scale low to yield our desired code value.
        return (low * intden + intden - 1) // range_val

    def scale(self, intlow, inthigh, intden):
        """Given an interval, scale the range to fit in the interval."""
        assert not self.encoding
        assert 0 <= intlow < inthigh <= intden <= self.half + 1
        range_val = self.range
        off = (range_val * intlow) // intden
        assert self.low >= off
        self.low -= off
        self.range = (range_val * inthigh) // intden - off

    def addbyte(self, byte):
        """Add an input byte to the decoding queue."""
        assert self.encoding and not self.finished
        qmask = self.qmask
        qlen = self.qlen
        qcount = self.qcount
        for i in range(7, -1, -1):
            qcount[qlen] = (byte >> i) & 1
            qlen = (qlen + 1) & qmask
        self.qlen = qlen

"""
import os
import sys
import struct

# Example compressor and decompressor using an adaptive order-0 symbol model.

# Parse arguments.
if len(sys.argv) != 4:
    print("3 arguments expected\npython RangeEncoder.py [-c|-d] infile outfile")
    exit()
mode, infile, outfile = sys.argv[1:]
if mode != "-c" and mode != "-d":
    print("mode must be -c or -d")
    exit()

res = 8
bit = 2 * res
size = 8 * res

# Adaptive order-0 symbol model.
prob = list(range(0, (size + 1) * bit, bit))


def incprob(sym):
    # Increment the probability of a given symbol.
    for i in range(sym + 1, size + 1):
        prob[i] += bit
    if prob[size] >= 65536:
        # Periodically halve all probabilities to help the model forget old symbols.
        for i in range(size, 0, -1):
            prob[i] -= prob[i - 1] - 1
        for i in range(1, size + 1):
            prob[i] = prob[i - 1] + (prob[i] >> 1)


def findsym(code):
    # Find the symbol who's cumulative interval encapsulates the given code.
    for sym in range(1, size + 1):
        if prob[sym] > code:
            return sym - 1


instream = open(infile, "rb")
outstream = open(outfile, "wb")
insize = os.path.getsize(infile)
buf = bytearray(1)

if mode == "-c":
    # Compress a file.
    enc = RangeEncoder(True)
    outstream.write(struct.pack(">i", insize))
    for inpos in range(insize + 1):
        if inpos < insize:
            # Encode a symbol.
            byte = ord(instream.read(1))
            enc.encode(prob[byte], prob[byte + 1], prob[size])
            incprob(byte)
        else:
            enc.finish()
        # While the encoder has bytes to output, output.
        while enc.hasbyte():
            buf[0] = enc.getbyte()
            outstream.write(buf)
else:
    # Decompress a file.
    dec = RangeEncoder(False)
    outsize = struct.unpack(">i", instream.read(4))[0]
    inpos, outpos = 4, 0
    while outpos < outsize:
        decode = dec.decode(prob[size])
        if decode is not None:
            # We are ready to decode a symbol.
            buf[0] = sym = findsym(decode)
            dec.scale(prob[sym], prob[sym + 1], prob[size])
            incprob(sym)
            outstream.write(buf)
            outpos += 1
        elif inpos < insize:
            # We need more input data.
            dec.addbyte(ord(instream.read(1)))
            inpos += 1
        else:
            # Signal that we have no more input data.
            dec.finish()

outstream.close()
instream.close()
"""

#------------------------------------------------------------------------------------------------------


class Packet:
    __slots__ = ['stream_id', 'sequence_number', 'compressed_payload', 'metadata', 'hamming_code']

    def __init__(self, stream_id, sequence_number, compressed_payload, metadata=None):
        self.stream_id = stream_id
        self.sequence_number = sequence_number
        self.compressed_payload = compressed_payload
        self.metadata = metadata if metadata is not None else {}
        self.hamming_code = self.generate_hamming_code()

    def generate_hamming_code(self):
        # Convert payload to bitarray
        payload_bits = bitarray.bitarray()
        payload_bits.frombytes(self.compressed_payload)

        # Calculate the number of parity bits needed
        parity_bits_count = 1
        while (2 ** parity_bits_count) < (len(payload_bits) + parity_bits_count + 1):
            parity_bits_count += 1

        # Initialize Hamming code with all zeros
        hamming_code = bitarray.bitarray(parity_bits_count + len(payload_bits))
        hamming_code.setall(0)

        # Copy payload bits to Hamming code, skipping parity bit positions
        i, j = 0, 0
        while i < len(hamming_code):
            if (i + 1) & i != 0:  # Check if i+1 is a power of 2
                i += 1  # Skip parity bits
                continue
            hamming_code[i] = payload_bits[j]
            i += 1
            j += 1

        # Calculate parity bits
        for i in range(parity_bits_count):
            mask = 1 << i  # bit mask to check corresponding bits
            count = 0
            for j in range(len(hamming_code)):
                if j & mask:  # if jth bit has 1 in its ith significant bit
                    count += hamming_code[j]
            hamming_code[mask - 1] = count % 2  # Set parity bit value

        return hamming_code.tobytes()

class DataMuxer:
    def __init__(self):
        self.streams = {}

    def add_stream(self, stream_id, data, metadata=None):
        compressed_data = self.compress_data(data)
        packets = self.packetize(stream_id, compressed_data, metadata)
        if stream_id not in self.streams:
            self.streams[stream_id] = []
        self.streams[stream_id].extend(packets)

    @staticmethod
    def compress_data(data):
        return zlib.compress(data)

    @staticmethod
    def packetize(stream_id, data, metadata=None, packet_size=100):
        packets = []
        num_packets = (len(data) + packet_size - 1) // packet_size
        for i in range(num_packets):
            start = i * packet_size
            end = min((i + 1) * packet_size, len(data))
            payload = data[start:end]
            packet = Packet(stream_id, i, payload, metadata)
            packets.append(packet)
        return packets

    def multiplex(self, loss_probability=0):
        multiplexed_data = []
        for stream_id, packets in self.streams.items():
            for packet in packets:
                if random.random() > loss_probability:
                    header = (packet.stream_id, len(packet.compressed_payload), packet.metadata)
                    multiplexed_data.append((header, packet.compressed_payload))
        return multiplexed_data

class DataDemuxer:
    def __init__(self):
        self.streams = {}

    def demultiplex(self, multiplexed_data, loss_probability=0):
        for header, compressed_payload in multiplexed_data:
            if random.random() > loss_probability:
                stream_id, compressed_payload_length, metadata = header
                corrected_payload = self.correct_hamming_code(compressed_payload)
                payload = self.decompress_data(corrected_payload)
                packet = Packet(stream_id, None, payload[:compressed_payload_length], metadata)
                self.add_packet(packet)

    @staticmethod
    def decompress_data(compressed_data):
        return zlib.decompress(compressed_data)

    def add_packet(self, packet):
        stream_id = packet.stream_id
        packets = self.streams.get(stream_id)
        if packets is None:
            packets = self.streams[stream_id] = {}
        packets[packet.sequence_number] = packet

    def correct_hamming_code(self, hamming_code):
        # Convert Hamming code to bitarray
        hamming_bits = bitarray.bitarray()
        hamming_bits.frombytes(hamming_code)

        # Detect and correct errors in Hamming code
        error_pos = 0
        for i in range(len(hamming_bits)):
            if (i + 1) & i != 0:  # Check if i+1 is a power of 2 (parity bit)
                parity = 0
                for j in range(len(hamming_bits)):
                    if j & (i + 1):  # If jth bit has 1 in its ith significant bit
                        parity ^= hamming_bits[j]
                if parity != hamming_bits[i]:  # If parity doesn't match, error detected
                    error_pos += i + 1

        if error_pos != 0 and error_pos <= len(hamming_bits):  # If error detected and within range
            hamming_bits.invert(error_pos - 1)  # Correct the error by flipping the bit

        return hamming_bits.tobytes()

    def get_stream_data(self, stream_id):
        packets = self.streams.get(stream_id)
        if packets:
            payload_bits = bitarray.bitarray()
            for packet in sorted(packets.values(), key=lambda pkt: pkt.sequence_number):
                payload_bits.frombytes(packet.compressed_payload)
            return payload_bits.tobytes()
        return b''

    def get_stream_metadata(self, stream_id):
        packets = self.streams.get(stream_id)
        if packets:
            return packets[sorted(packets.keys())[0]].metadata
        return {}