TL-R
RS485 Bus Integrated Controller
User Manual

Contents
Chapter I Product Introduction ............................................................................................................................................... 1
1.1 Product Overview ............................................................................................................................................................. 1
1.2 Communication Specifications ......................................................................................................................................... 1
1.3 Product Specifications ....................................................................................................................................................... 1
1.2 Installation Dimensions ..................................................................................................................................................... 2
Chapter 2: Drive Ports and Wiring ......................................................................................................................................... 4
2.1 Drive Port Definitions ....................................................................................................................................................... 4
2.1.1 RS485 Communication Port ....................................................................................................................................... 4
2.1.2 Power Port ................................................................................................................................................................. 4
2.1.3 DI/DO Port ................................................................................................................................................................ 4
2.2 Wiring ............................................................................................................................................................................... 5
2.2.1 Drive Wiring Diagram ............................................................................................................................................... 5
2.2.2 DI/DO Port Usage Instructions ................................................................................................................................. 5
2.2.4 Dip Switch Settings .................................................................................................................................................... 7
Chapter 3: Communication Control Instructions .................................................................................................................. 8
3.1 Position Mode ................................................................................................................................................................... 8
3.1.1 Related Parameters .................................................................................................................................................... 8
3.1.2 Position Mode Description ........................................................................................................................................ 8
3.1.3 Control Method Explanation ...................................................................................................................................... 8
3.2 Internal Multi-Segment Positioning .................................................................................................................................. 9
3.2.1 Related Parameters .................................................................................................................................................... 9
3.2.2 Internal Multi-Segment Position Control Instructions ............................................................................................... 9
3.3 Internal Multi-Segment Speed ........................................................................................................................................ 10
3.3.1 Related Parameters .................................................................................................................................................. 10
3.2.2 Internal Multi-Segment Position Control Instructions .............................................................................................. 11
3.4 Homing Mode .................................................................................................................................................................. 11
3.4.1 Related Parameters ................................................................................................................................................... 11
3.4.2 Homing Mode Description ....................................................................................................................................... 12
3.4.3 Control Procedure Description ................................................................................................................................ 13
3.5 Detailed Parameter Description ...................................................................................................................................... 13
3.5.1 Monitoring Parameters ............................................................................................................................................ 13
3.5.2 DI/DO Parameters ................................................................................................................................................... 14
3.5.3 Communication Control Parameters ....................................................................................................................... 15
3.5.4 Internal Multi-Segment Positioning ......................................................................................................................... 17
3.5.5 Internal Multi-Segment Speed .................................................................................................................................. 19
3.5.6 Manufacturer Parameters ........................................................................................................................................ 20
3.6 Alarm Handling ............................................................................................................................................................... 21
Chapter 4: MODBUS RTU Instructions ............................................................................................................................... 21
4.1 Read Parameter Command (0x03) .................................................................................................................................. 21
4.2 Write to a single register (0x06) ...................................................................................................................................... 22
4.3 Write Multiple Registers Command (0x10) .................................................................................................................... 23
4.4 Exception Responses and Error Codes ............................................................................................................................ 23

User Manuel for RS485 Bus Integrated Controller
Chapter I Product Introduction
1.1 Product Overview
This series of stepper drive integrated controller adopts the latest generation 32-bit DSP technology and integrates
RS485 bus control functions. It supports the MODBUS-RTU communication protocol and can connect up to 32 axes,
enabling multi-axis bus synchronization control. The driver features 15 internal position settings and 15 internal speed
settings, supporting functions such as automatic homing, absolute/relative positioning, JOG operations, and more. It can
be directly controlled using a touchscreen or a controller with an RS485 interface.
1.2 Communication Specifications
➢ Communication Interface: RS485
➢ Communication Protocol: Modbus RTU
➢ Baud Rates: 9600, 19200, 38400, 115200 (configured via SW5 dip switch)
➢ Station Number: 1-31 (configured via SW1-SW4 dip switches)
➢ Terminal Resistance: 120Ω (configured via SW6 dip switch)
➢ Parity: No parity (default), Odd parity, Even parity
1.3 Product Specifications
Driver Models TLC42-R TLO42-R TLC57-R TLO57-R TLC60-R TLO60-R TLC86-R TLO86-R
Compatible
42 57 60 86
Motor Sizes
Power Supply
20～36V DC 24～50V DC 24～50V DC 24～70V DC
Voltage
Maximum
2.0A 4.0A 4.0A 6.0A
Output Current
DI Port Input
10 ~ 50mA
Current
DI Port Input
24V DC
Voltage
Encoder 1000 lines None 1000 lines None 1000 lines None 1000 lines None
Insulation
100MΩ
Resistance
Temperature: 0°C ~ 45°C;
Humidity: ≤90% RH, non-condensing
Operating
Altitude: ≤1000m.
Environment
Installation Conditions: Free from corrosive gases, flammable gases, oil mist, or dust.
Vibration: Less than 0.5G (4.9m/s²), 10–60 Hz (non-continuous operation).
Storage
-20℃ to 65℃ (no frost), ≤90% RH, non-condensing
Environment:
1

User Manuel for RS485 Bus Integrated Controller
1.4 Installation Dimensions
TLC42-C/TLO42-C
TLC57-C/TLO57-C
TLC60-C/TLO60-C
2

User Manuel for RS485 Bus Integrated Controller

TLC86-C/TLO86-C

| Model                 | D             | Motor Length  | Total Body Length (L)  |
| --------------------- | ------------- | ------------- | ---------------------- |
| TLC42-R/ TLO42-R-04   | φ5            | 48            | 75                     |
| TLC42-R/ TLO42-R-08   | φ5            | 60            | 87                     |
| TLC57-R/ TLO57-R-1    | φ6.35 or φ8   | 56            | 84.2                   |
| TLC57-R/ TLO57-R-2    | φ6.35 or φ8   | 82            | 110.2                  |
| TLC57-R/ TLO57-R-3    | φ6.35 or φ8   | 100           | 128.2                  |
| TLC60-R/ TLO60-R-3    | φ8            | 88            | 119.2                  |
| TLC60-R/ TLO60-R-3.5  | φ8            | 100           | 131.2                  |
| TLC60-R/ TLO60-R-4    | φ8            | 112           | 143.2                  |
| TLC86-R/ TLO86-R-4.5  | φ12.7 or φ14  | 80            | 125.2                  |
| TLC86-R/ TLO86-R-8.5  | φ12.7 or φ14  | 114           | 159.2                  |
| TLC86-R/ TLO86-R-10   | φ12.7 or φ14  | 128           | 173.2                  |
| TLC86-R/ TLO86-R-12   | φ12.7 or φ14  | 150           | 195.2                  |

3

User Manuel for RS485 Bus Integrated Controller
Chapter 2: Drive Ports and Wiring
2.1 Drive Port Definitions
2.1.1 RS485 Communication Port
|     |     | Pin  | Signal Definition  |       |
| --- | --- | ---- | ------------------ | ----- |
|     |     | 1    |                    | 485-  |
|     |     | 2    |                    | 485+  |
|     |     | 3    | GND                |       |
|     |     | 4    |                    | 485+  |
|     |     | 5    |                    | 485-  |

2.1.2 Power Port
| Pin  | Definitions  |     | Description  |     |
| ---- | ------------ | --- | ------------ | --- |
DC Power Negative Terminal
| 1   | VDC  | TL42    | TL57/TL60  | TL86    |
| --- | ---- | ------- | ---------- | ------- |
|     |      | 24～36V  | 24～50V     | 24～70V  |

| 2   | GND  | DC Power Negative Terminal  |     |     |
| --- | ---- | --------------------------- | --- | --- |

2.1.3 DI/DO Port
|     |     | Pin  Definitions  |     | Description  |
| --- | --- | ----------------- | --- | ------------ |
|     |     | 1  DI0            |     |              |
|     |     | 2  DI1            |     |              |
Single-ended input;
|     |     | 3  DI2  |     |     |
| --- | --- | ------- | --- | --- |
operating voltage 24V
|     |     | 4  DI3  |     |     |
| --- | --- | ------- | --- | --- |
|     |     | 5  DI4  |     |     |
Common input;
supports
6  DICOM
sinking/sourcing
configurations
7  DO0+
Differential output 1
8  DO0-
9  DO1+
Differential output 2
10  DO1-

4

User Manuel for RS485 Bus Integrated Controller
2.2 Wiring
2.2.1 Drive Wiring Diagram
485 Bus Integrated Machine
Home
Position
Positive
Limit
Negative
Limit
485 Communication
Interface
Alarm
Output
Brake
Switching Power
Release
Supply
42 (DC18V-DC36V) Recommended 24V
57 (DC24V-DC48V) Recommended 36V
86 (DC24V-DC48V) Recommended 48V
Notes: 1. The DI input voltage is 24V. If it exceeds 24V, a current-limiting resistor is required.
2. The DI input wiring supports both sourcing and sinking configurations. When DICOM is 24V,
DI is activated by connecting to 0V; when DICOM is 0V, DI is activated by connecting to 24V.
3. The DO common terminal DOCOM can only be connected to 0V and not to 24V.
2.2.2 DI/DO Port Usage Instructions
This series of drivers provides 5 programmable input interfaces and 2 programmable output interfaces.
Each DI/DO function can be configured via the RS485 bus using the upper computer debugging software.
The relevant configuration parameters are shown in the table below:
5

User Manuel for RS485 Bus Integrated Controller
Parameter No.  Address (Decimal)  Description  Default Value
|     | PA_010  |     | 16  | DI terminal normally open/closed switching  |                                  |     |     | 0   |
| --- | ------- | --- | --- | ------------------------------------------- | -------------------------------- | --- | --- | --- |
|     | PA_011  |     | 17  |                                             | Configure DI input port 0        |     |     | 1   |
|     | PA_012  |     | 18  |                                             | Configure DI input port 1        |     |     | 2   |
|     | PA_013  |     | 19  |                                             | Configure DI input port 2        |     |     | 3   |
|     | PA_014  |     | 20  |                                             | Configure DI input port 3        |     |     | 0   |
|     | PA_015  |     | 21  |                                             | Configure DI input port 4        |     |     | 0   |
|     | PA_01A  |     | 26  |                                             | Input port filter coefficient    |     |     | 2   |
|     | PA_01B  |     | 27  | DO terminal normally open/closed switching  |                                  |     |     | 0   |
|     | PA_01C  |     | 28  |                                             | Configure DO output port 0       |     |     | 1   |
|     | PA_01D  |     | 29  |                                             | Configure DO output port 1       |     |     | 0   |
|     | PA_01F  |     | 31  |                                             | Force output of the output port  |     |     | 0   |

DI Port Function Command Table:
Command Value  Function Description  Command Value  Function Description
|     | 0   |                        | Undefined       |     |     | 10  | Negative JOG             |     |
| --- | --- | ---------------------- | --------------- | --- | --- | --- | ------------------------ | --- |
|     | 1   |                        | Homing signal   |     |     | 11  | Homing trigger           |     |
|     | 2   |                        | Positive limit  |     |     | 12  | Position path trigger    |     |
|     | 3   |                        | Negative limit  |     |     | 13  | Speed path trigger       |     |
|     | 4   |                        | Release signal  |     |     | 14  | Path selection switch 0  |     |
|     | 5   |                        | Stop signal     |     |     | 15  | Path selection switch 1  |     |
|     | 6   | Forced emergency stop  |                 |     |     | 16  | Path selection switch 2  |     |
|     | 9   |                        | Positive JOG    |     |     | 17  | Path selection switch 3  |     |

DO Port Function Command Table:
Command
| Command Value  |     | Function Description  |     |     |     |     | Function Description  |     |
| -------------- | --- | --------------------- | --- | --- | --- | --- | --------------------- | --- |
Value
|     | 0   |     | Undefined           |     |     | 5   | Brake release signal     |     |
| --- | --- | --- | ------------------- | --- | --- | --- | ------------------------ | --- |
|     | 1   |     | Alarm output        |     |     | 9   | Forced output control 1  |     |
|     | 2   |     | Motor Running       |     |     | 10  | Forced output control 2  |     |
|     | 3   |     | Homing Complete     |     |     | 11  | Forced output control 3  |     |
|     | 4   |     | In-position signal  |     |     |     |                          |     |
DO Port Forced Output Control Method:
| PA_01F Corresponding Bit  |     |     |     |     |     | Description  |     |     |
| ------------------------- | --- | --- | --- | --- | --- | ------------ | --- | --- |
Bit0  Controls the output port with function command set to 9. 0: Off, 1: On
Bit1  Controls the output port with function command set to 10. 0: Off, 1: On

6

User Manuel for RS485 Bus Integrated Controller
2.2.4 Dip Switch Settings
  This series of RS485 bus integrated controllers has a 6-position dip switch used to set the RS485 station number,
communication baud rate, and terminal resistance. The configuration is shown below:
|     |     | SW1  SW2  | SW3  | SW4  SW5  | SW6  |     |
| --- | --- | --------- | ---- | --------- | ---- | --- |
|     |     |           |      | 丨         | 丨    |     |

|     |     | Station Number Setting  |     | Baud Rate Terminal Resistance  |     |     |
| --- | --- | ----------------------- | --- | ------------------------------ | --- | --- |

Baud Rate Setting:
|     |     | Baud Rate  |     | SW5  |     |     |
| --- | --- | ---------- | --- | ---- | --- | --- |
|     |     | 115200     |     | OFF  |     |     |
|     |     | Custom     |     | ON   |     |     |
Terminal resistance settingWhen SW5 is ON, the baud rate can be modified through PA-28 (Decimal Address 40): 0: 115200;
1: 38400; 2: 19200; 3: 9600.
Terminal Resistance Setting:
When SW6 is set to ON, a 120Ω terminal resistance is connected between the signal lines to prevent signal reflection at
the end of the cable.

Driver Station Number Settings:
| Station number  |         | SW1  | SW2  |     | SW3  | SW4  |
| --------------- | ------- | ---- | ---- | --- | ---- | ---- |
|                 | Custom  | OFF  | OFF  |     | OFF  | OFF  |
|                 | 1       | ON   | OFF  |     | OFF  | OFF  |
|                 | 2       | OFF  | ON   |     | OFF  | OFF  |
|                 | 3       | ON   | ON   |     | OFF  | OFF  |
|                 | 4       | OFF  | OFF  |     | ON   | OFF  |
|                 | 5       | ON   | OFF  |     | ON   | OFF  |
|                 | 6       | OFF  | ON   |     | ON   | OFF  |
|                 | 7       | ON   | ON   |     | ON   | OFF  |
|                 | 8       | OFF  | OFF  |     | OFF  | ON   |
|                 | 9       | ON   | OFF  |     | OFF  | ON   |
|                 | 10      | OFF  | ON   |     | OFF  | ON   |
|                 | 11      | ON   | ON   |     | OFF  | ON   |
|                 | 12      | OFF  | OFF  |     | ON   | ON   |
|                 | 13      | ON   | OFF  |     | ON   | ON   |
|                 | 14      | OFF  | ON   |     | ON   | ON   |
|                 | 15      | ON   | ON   |     | ON   | ON   |

7

User Manuel for RS485 Bus Integrated Controller
Chapter 3: Communication Control Instructions
3.1 Position Mode
3.1.1 Related Parameters
| Parameter  |      | Address    |     |     |       |                |     |     |            |             |
| ---------- | ---- | ---------- | --- | --- | ----- | -------------- | --- | --- | ---------- | ----------- |
|            |      |            |     |     | Name  | Setting Range  |     |     | Data Type  | Attributes  |
|            | No.  | (Decimal)  |     |     |       |                |     |     |            |             |
PA_033  51  Positioning Start Speed (r/min)  0～3000  UNSIGNED16  RW
PA_034  Positioning Acceleration Time (ms)  0～2000  UNSIGNED16  RW
52
PA_035  Positioning Deceleration Time (ms)  0～2000  UNSIGNED16  RW
53
| PA_036  |     |     |     |                                |                            |               | 0～3000  |             |     |     |
| ------- | --- | --- | --- | ------------------------------ | -------------------------- | ------------- | ------- | ----------- | --- | --- |
|         |     | 54  |     |                                | Positioning Speed (r/min)  |               |         | UNSIGNED16  |     | RW  |
| PA_037  |     | 55  |     | Positioning Target (Pulses) H  |                            | -2147483648~  |         |             |     |     |
|         |     |     |     |                                |                            |               |         | INTEGER32   |     | RW  |
| PA_038  |     |     |     |                                |                            | 2147483647    |         |             |     |     |
|         |     | 56  |     | Positioning Target (Pulses) L  |                            |               |         |             |     |     |
PA_04E
|        |        | 78  |     |                              | Control Word           |     | 0 ~ 127  | UNSIGNED16  |     | RW  |
| ------ | ------ | --- | --- | ---------------------------- | ---------------------- | --- | -------- | ----------- | --- | --- |
|        | PA_04  | 4   |     |                              | Operating Status       |     |          | UNSIGNED16  |     | RO  |
|        | PA_08  | 8   |     | Current Position (Pulses) H  |                        |     |          |             |     |     |
|        |        |     |     |                              |                        |     |          | INTEGER32   |     | RO  |
|        | PA_09  | 9   |     | Current Position (Pulses) L  |                        |     |          |             |     |     |
| PA_0A  |        | 10  |     |                              | Current Speed (r/min)  |     |          | INTEGER16   |     | RO  |
3.1.2 Position Mode Description
In position mode, the master station specifies the motion parameters: start speed (0x0033), acceleration time (0x0034),
deceleration time (0x0035), running speed (0x0036), and positioning target (0x0037, 0x0038). The driver internally
constructs a motion path based on these parameters to achieve precise position control. The motion curve is shown in the
diagram below:
|     |     |     |     | ）mpr（度速 |     | Target Speed  目标速度 |     |     |     |     |
| --- | --- | --- | --- | ------- | --- | ------------------ | --- | --- | --- | --- |

d e Tar目ge标t P位osi置tion
e
p (Pulse Count)
S （脉冲数）

Initi起al S始pe速ed度
T时im间e
|     |     |     |     |     | Acceleration  加速时间 | 减速时间 Deceleration  |       |        |     |     |
| --- | --- | --- | --- | --- | ------------------ | ------------------ | ----- | ------ | --- | --- |
|     |     |     |     |     |                    |                    |       | （  ms） |     |     |
|     |     |     |     |     | Time               |                    | Time  |        |     |     |
|     |     |     |     |     |                    |                    |       |        |     |     |
3.1.3 Control Method Explanation
1. Control Word Explanation: The control word (0x004E) uses Bit0-Bit6 for control, with each bit corresponding to a function
as shown below:
| Control Word Bit  |     |     | Function  |     |     |     | Description  |     |     |     |
| ----------------- | --- | --- | --------- | --- | --- | --- | ------------ | --- | --- | --- |
Bit0  Positioning Control    0: Inactive; 1: Active (no reset needed, simply set to 1 again)
Bit1  Positioning Mode    0: Relative position; 1: Absolute position
0: Ignore new command if a positioning motion is in progress
|     | Bit2  |     | Switch Mode  |     |     |     |     |     |     |     |
| --- | ----- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
1: Interrupt current positioning motion to execute new command;
|     | Bit3  |     | JOG Control  |     |     |     | 0: Inactive; 1: Active;  |     |     |     |
| --- | ----- | --- | ------------ | --- | --- | --- | ------------------------ | --- | --- | --- |
Bit4  Homing Control  0: Inactive; 1: Active (no reset needed, simply set to 1 again)
|     | Bit5  |                         | Stop Control  |     |     |     | 0: Inactive; 1: Active;  |     |     |     |
| --- | ----- | ----------------------- | ------------- | --- | --- | --- | ------------------------ | --- | --- | --- |
|     | Bit6  | Emergency Stop Control  |               |     |     |     | 0: Inactive; 1: Active;  |     |     |     |
8

User Manuel for RS485 Bus Integrated Controller
Status Word Explanation: By monitoring the status word (0x0004) Bit0-Bit6, the current motion status can be
determined as shown below:
| Status Word Bit  |       |     |     | Function         |        |     | Status Word Bit  |       |     | Function             |     |     |
| ---------------- | ----- | --- | --- | ---------------- | ------ | --- | ---------------- | ----- | --- | -------------------- | --- | --- |
|                  | Bit0  |     |     | In position      |        |     |                  | Bit4  |     | Motor Enabled        |     |     |
|                  | Bit1  |     |     | Homing Complete  |        |     |                  | Bit5  |     | Positive Soft Limit  |     |     |
|                  | Bit2  |     |     | Motor Running    |        |     |                  | Bit6  |     | Negative Soft Limit  |     |     |
|                  | Bit3  |     |     |                  | Fault  |     |                  |       |     |                      |     |     |
3.2 Internal Multi-Segment Positioning
3.2.1 Related Parameters
| Parameter  |     | Address    |                                |     |       |     |     |                |            |            |     |             |
| ---------- | --- | ---------- | ------------------------------ | --- | ----- | --- | --- | -------------- | ---------- | ---------- | --- | ----------- |
|            |     |            |                                |     | Name  |     |     | Setting Range  |            | Data Type  |     | Attributes  |
| No.        |     | (Decimal)  |                                |     |       |     |     |                |            |            |     |             |
| PA_050     |     | 80         | Positioning Path 0 (Pulses) H  |     |       |     |     | -2147483648~   |            |            |     |             |
|            |     |            |                                |     |       |     |     |                | INTEGER32  |            |     | RW          |
| PA_051     |     | 81         | Positioning Path 0 (Pulses) L  |     |       |     |     | 2147483647     |            |            |     |             |
0～3000
| PA_052  |     | 82  |     | Positioning Path 0 Speed  |     |     |     |     | UNSIGNED16  |     |     | RW  |
| ------- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
Positioning Path 0 Acceleration
| PA_053  |     | 83  |     |     |     |     |     | 0～2000  | UNSIGNED16  |     |     | RW  |
| ------- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | --- | --- |
Time
Positioning Path 0 Deceleration
0～2000
| PA_054  |     | 84  |     |     |     |     |     |     | UNSIGNED16  |     |     | RW  |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- |
Time
| PA_056  |     | 86  | Positioning Path 1 (Pulses) H  |     |     |     |     | -2147483648~  |            |     |     |     |
| ------- | --- | --- | ------------------------------ | --- | --- | --- | --- | ------------- | ---------- | --- | --- | --- |
|         |     |     |                                |     |     |     |     |               | INTEGER32  |     |     | RW  |
| PA_057  |     | 87  | Positioning Path 1 (Pulses) L  |     |     |     |     | 2147483647    |            |     |     |     |
PA_058  88  Positioning Path 1 Speed  0～3000  UNSIGNED16  RW
Positioning Path 1 Acceleration
| PA_059  |     | 89  |     |     |     |     |     | 0～2000  | UNSIGNED16  |     |     | RW  |
| ------- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | --- | --- |
Time
Positioning Path 1 Deceleration
| PA_05A  |     | 90  |     |     |     |     |     | 0～2000  | UNSIGNED16  |     |     | RW  |
| ------- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | --- | --- |
Time
...
| PA_0AA  |     | 170  | Positioning Path 15 (Pulses) H  |     |     |     |     | -2147483648~  |            |     |     |     |
| ------- | --- | ---- | ------------------------------- | --- | --- | --- | --- | ------------- | ---------- | --- | --- | --- |
|         |     |      |                                 |     |     |     |     |               | INTEGER32  |     |     | RW  |
| PA_0AB  |     | 171  | Positioning Path 15 (Pulses) L  |     |     |     |     | 2147483647    |            |     |     |     |
PA_0AC  172  Positioning Path 15 Speed  0～3000  UNSIGNED16  RW
Positioning Path 15
| PA_0AD  |     | 173  |     |     |     |     |     | 0～2000  | UNSIGNED16  |     |     | RW  |
| ------- | --- | ---- | --- | --- | --- | --- | --- | ------- | ----------- | --- | --- | --- |
Acceleration Time
Positioning Path 15
| PA_0AE  |     | 174  |     |     |     |     |     | 0～2000  | UNSIGNED16  |     |     | RW  |
| ------- | --- | ---- | --- | --- | --- | --- | --- | ------- | ----------- | --- | --- | --- |
Deceleration Time
|        |     |     |     |                              |     |     |     |     |             |     |     |     |
| ------ | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
| PA_04  |     | 4   |     | Operating Status             |     |     |     |     | UNSIGNED16  |     |     | RO  |
| PA_08  |     | 8   |     | Current Position (Pulses) H  |     |     |     |     |             |     |     |     |
|        |     |     |     |                              |     |     |     |     | INTEGER32   |     |     | RO  |
| PA_09  |     | 9   |     | Current Position (Pulses) L  |     |     |     |     |             |     |     |     |
| PA_0A  |     | 10  |     | Current Speed (r/min)        |     |     |     |     | INTEGER16   |     |     | RO  |
3.2.2 Internal Multi-Segment Position Control Instructions
1. The internal multi-segment positioning requires selection and triggering through the DI ports. The specific configuration is
as follows:
Parameter No.  Address (Decimal)  Setting Value  Description
| PA_011  |     |     | 17  |     |     | 12  |     | DI0 configured as position path trigger    |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- |
| PA_012  |     |     | 18  |     |     | 14  |     | DI1 configured as path selection switch 0  |     |     |     |     |
9

User Manuel for RS485 Bus Integrated Controller
|     | PA_013  |     |     | 19  |     |     |     | 15  |     | DI2 configured as path selection switch 1  |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- |
|     | PA_014  |     |     | 20  |     |     |     | 16  |     | DI3 configured as path selection switch 2  |     |     |     |
|     | PA_015  |     |     | 21  |     |     |     | 17  |     | DI4 configured as path selection switch 3  |     |     |     |
After configuring the DI ports as per the table above, the position segment is selected using DI1-DI4 and then
triggered (rising edge) by DI0 to execute the position segment. The corresponding table is as follows:
|            |      |            |            |            |      |                |     |     | Position  |     | Position  | Accel    | Deceleration  |
| ---------- | ---- | ---------- | ---------- | ---------- | ---- | -------------- | --- | --- | --------- | --- | --------- | -------- | ------------- |
| Selection  |      | Selection  | Selection  | Selection  |      | Corresponding  |     |     |           |     |           |          |               |
|            |      |            |            |            |      |                |     |     | Pulse     |     | Speed     | Time     | Time          |
| Switch 0   |      | Switch 1   | Switch 2   | Switch 3   |      | Position Path  |     |     |           |     |           |          |               |
|            |      |            |            |            |      |                |     |     | Address   |     | Address   | Address  | Address       |
|            | OFF  | OFF        | OFF        |            | OFF  |                | 0   |     | 80/ 81    |     | 82        | 83       | 84            |
|            | ON   | OFF        | OFF        |            | OFF  |                | 1   |     | 86/ 87    |     | 88        | 89       | 90            |
|            | OFF  | ON         | OFF        |            | OFF  |                | 2   |     | 92/ 93    |     | 94        | 95       | 96            |
|            | ON   | ON         | OFF        |            | OFF  |                | 3   |     | 98/ 99    |     | 100       | 101      | 102           |
|            | OFF  | OFF        | ON         |            | OFF  |                | 4   |     | 104/105   |     | 106       | 107      | 108           |
|            | ON   | OFF        | ON         |            | OFF  |                | 5   |     | 110/ 111  |     | 112       | 113      | 114           |
|            | OFF  | ON         | ON         |            | OFF  |                | 6   |     | 116/ 117  |     | 118       | 119      | 120           |
|            | ON   | ON         | ON         |            | OFF  |                | 7   |     | 122/123   |     | 124       | 125      | 126           |
|            | OFF  | OFF        | OFF        |            | ON   |                | 8   |     | 128/129   |     | 130       | 131      | 132           |
|            | ON   | OFF        | OFF        |            | ON   |                | 9   |     | 134/135   |     | 136       | 137      | 138           |
|            | OFF  | ON         | OFF        |            | ON   |                | 10  |     | 140/141   |     | 142       | 143      | 144           |
|            | ON   | ON         | OFF        |            | ON   |                | 11  |     | 146/147   |     | 148       | 149      | 150           |
|            | OFF  | OFF        | ON         |            | ON   |                | 12  |     | 152/153   |     | 154       | 155      | 156           |
|            | ON   | OFF        | ON         |            | ON   |                | 13  |     | 158/159   |     | 160       | 161      | 162           |
|            | OFF  | ON         | ON         |            | ON   |                | 14  |     | 164/165   |     | 166       | 167      | 168           |
|            | ON   | ON         | ON         |            | ON   |                | 15  |     | 170/171   |     | 172       | 173      | 174           |
2. Internal Multi-Segment Position Mode Settings:
| Parameter  |      |     | Address    |                      |     |     |     | Default  |     |     |     |              |     |
| ---------- | ---- | --- | ---------- | -------------------- | --- | --- | --- | -------- | --- | --- | --- | ------------ | --- |
|            |      |     |            | Function Definition  |     |     |     |          |     |     |     | Description  |     |
|            | No.  |     | (Decimal)  |                      |     |     |     | Value    |     |     |     |              |     |
0: Interrupt current positioning motion to
Internal Multi-Segment
execute new command;
|     | PA_026  |     | 38  |     | Position  |     |     |     | 0   |     |     |     |     |
| --- | ------- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
1: Ignore new command if a positioning
 Trigger Mode
motion is in progress
Internal Multi-Segment
|     |         |     |     |                    | Position  |     |     |     |     |     | 0: Relative position mode;  |     |     |
| --- | ------- | --- | --- | ------------------ | --------- | --- | --- | --- | --- | --- | --------------------------- | --- | --- |
|     | PA_04A  |     | 74  |                    |           |     |     |     | 0   |     |                             |     |     |
|     |         |     |     | Absolute/Relative  |           |     |     |     |     |     | 1: Absolute position mode   |     |     |
Position Mode

3.3 Internal Multi-Segment Speed
3.3.1 Related Parameters
| Parameter  |      |     | Address    |     |     |       |     |     |     |                |     |            |             |
| ---------- | ---- | --- | ---------- | --- | --- | ----- | --- | --- | --- | -------------- | --- | ---------- | ----------- |
|            |      |     |            |     |     | Name  |     |     |     | Setting Range  |     | Data Type  | Attributes  |
|            | No.  |     | (Decimal)  |     |     |       |     |     |     |                |     |            |             |
PA_0B0  176  Speed Path 0 Running Speed  -3000～3000  INTEGER16  RW
PA_0B1  177  Speed Path 0 Acceleration Time  0～2000  UNSIGNED16  RW
PA_0B2  178  Speed Path 0 Deceleration Time  0～2000  UNSIGNED16  RW
PA_0B3  179  Speed Path 1 Running Speed  -3000～3000  INTEGER16  RW
PA_0B4  180  Speed Path 1 Acceleration Time  0～2000  UNSIGNED16  RW
10

User Manuel for RS485 Bus Integrated Controller
PA_0B5  181  Speed Path 1 Deceleration Time  0～2000  UNSIGNED16  RW
...
PA_0DD  221  Speed Path 15 Running Speed  -3000～3000  INTEGER16  RW
PA_0DE  222  Speed Path 15 Acceleration Time  0～2000  UNSIGNED16  RW
PA_0DF  223  Speed Path 15 Deceleration Time  0～2000  UNSIGNED16  RW
|     | PA_04  |     | 4   |     | Operating Status       |     |     |     | UNSIGNED16  | RO  |
| --- | ------ | --- | --- | --- | ---------------------- | --- | --- | --- | ----------- | --- |
|     | PA_0A  |     | 10  |     | Current Speed (r/min)  |     |     |     | INTEGER16   | RO  |
3.2.2 Internal Multi-Segment Position Control Instructions
The internal multi-segment speed needs to be selected and triggered via DI ports to operate, as described below:
Parameter No.  Address (Decimal)  Setting Value  Description
|     | PA_011  |     |     | 17  |     | 13  |     | DI0 configured as speed path trigger       |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- |
|     | PA_012  |     |     | 18  |     | 14  |     | DI1 configured as path selection switch 0  |     |     |
|     | PA_013  |     |     | 19  |     | 15  |     | DI2 configured as path selection switch 1  |     |     |
|     | PA_014  |     |     | 20  |     | 16  |     | DI3 configured as path selection switch 2  |     |     |
|     | PA_015  |     |     | 21  |     | 17  |     | DI4 configured as path selection switch 3  |     |     |
After configuring the DI ports as per the table above, the speed segment is selected using DI1-DI4 and then
triggered (connect to run, disconnect to stop) by DI0 to execute the speed segment. The corresponding table is as
follows:
|     |     |     |     |     |     |     |     | Running  |     | Deceleration  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------------- |
Selection  Selection  Selection  Selection  Corresponding  Accel Time
|           |      |           |     |           |           |             |     | Speed    |          | Time     |
| --------- | ---- | --------- | --- | --------- | --------- | ----------- | --- | -------- | -------- | -------- |
| Switch 0  |      | Switch 1  |     | Switch 2  | Switch 3  | Speed Path  |     |          | Address  |          |
|           |      |           |     |           |           |             |     | Address  |          | Address  |
|           | OFF  | OFF       |     | OFF       | OFF       | 0           |     | 176      | 177      | 178      |
|           | ON   | OFF       |     | OFF       | OFF       | 1           |     | 179      | 180      | 181      |
|           | OFF  | ON        |     | OFF       | OFF       | 2           |     | 182      | 183      | 184      |
|           | ON   | ON        |     | OFF       | OFF       | 3           |     | 185      | 186      | 187      |
|           | OFF  | OFF       |     | ON        | OFF       | 4           |     | 188      | 189      | 190      |
|           | ON   | OFF       |     | ON        | OFF       | 5           |     | 191      | 192      | 193      |
|           | OFF  | ON        |     | ON        | OFF       | 6           |     | 194      | 195      | 196      |
|           | ON   | ON        |     | ON        | OFF       | 7           |     | 197      | 198      | 199      |
|           | OFF  | OFF       |     | OFF       | ON        | 8           |     | 200      | 201      | 202      |
|           | ON   | OFF       |     | OFF       | ON        | 9           |     | 203      | 204      | 205      |
|           | OFF  | ON        |     | OFF       | ON        | 10          |     | 206      | 207      | 208      |
|           | ON   | ON        |     | OFF       | ON        | 11          |     | 209      | 210      | 211      |
|           | OFF  | OFF       |     | ON        | ON        | 12          |     | 212      | 213      | 214      |
|           | ON   | OFF       |     | ON        | ON        | 13          |     | 215      | 216      | 217      |
|           | OFF  | ON        |     | ON        | ON        | 14          |     | 218      | 219      | 220      |
|           | ON   | ON        |     | ON        | ON        | 15          |     | 221      | 222      | 223      |
3.4 Homing Mode
3.4.1 Related Parameters
| Parameter  |      |     | Address    |     |       |     |                |     |            |             |
| ---------- | ---- | --- | ---------- | --- | ----- | --- | -------------- | --- | ---------- | ----------- |
|            |      |     |            |     | Name  |     | Setting Range  |     | Data Type  | Attributes  |
|            | No.  |     | (Decimal)  |     |       |     |                |     |            |             |
PA_040  64  Homing Mode  17, 18, 24, 29, 35  UNSIGNED 16  RW
11

User Manuel for RS485 Bus Integrated Controller
| PA_041  | 65  | Homing Speed        | 0～3000  | UNSIGNED16  | RW  |
| ------- | --- | ------------------- | ------- | ----------- | --- |
| PA_042  | 66  | Homing Creep Speed  | 0～3000  | UNSIGNED16  | RW  |
Homing Acceleration/
0～2000
| PA_043  | 67  |     |     | INTEGER16  | RW  |
| ------- | --- | --- | --- | ---------- | --- |
Deceleration Time
| PA_044  | 68  | Home Offset Value H          | -2147483648~  |             |     |
| ------- | --- | ---------------------------- | ------------- | ----------- | --- |
|         |     |                              |               | INTEGER32   | RW  |
| PA_045  | 69  | Home Offset Value L          | 2147483647    |             |     |
| PA_04   | 4   | Operating Status             |               | UNSIGNED16  | RO  |
| PA_08   | 8   | Current Position (Pulses) H  |               |             |     |
|         |     |                              |               | INTEGER32   | RO  |
| PA_09   | 9   | Current Position (Pulses) L  |               |             |     |
| PA_0A   | 10  | Current Speed (r/min)        |               | INTEGER16   | RO  |
3.4.2 Homing Mode Description
1. Negative Limit Mode (PA_040=17): After initiating homing, the motor runs in the negative direction at the
homing speed (PA_041). When the negative limit switch is detected, the motor decelerates and stops. Then, the
motor runs a certain distance in the positive direction at the homing speed (PA_041) and stops after decelerating.
The motor then runs in the negative direction at the homing creep speed (PA_042). When the negative limit switch
is detected again, the motor stops, completing the homing process.
Nega负tiv限e L位im开it 关Switch

2. Positive Limit Mode (PA_040=18): After initiating homing, the motor runs in the positive direction at the
homing speed (PA_041). When the positive limit switch is detected, the motor decelerates and stops. Then, the
motor runs a certain distance in the negative direction at the homing speed (PA_041) and stops after decelerating.
The motor then runs in the positive direction at the homing creep speed (PA_042). When the positive limit switch is
detected again, the motor stops, completing the homing process.
Pos正itiv限e L位im开it S关witch

3. Positive Origin Mode (PA_040 = 24):After initiating the homing process, the motor moves in the positive
direction at the homing speed (PA_041). When the origin switch is detected, the motor decelerates and stops. It then
moves a short distance in the negative direction at the homing speed (PA_041) and stops. The motor then moves in
the positive direction at the homing creep speed (PA_042). When the origin switch is detected again, the motor
stops, completing the homing process.
12

User Manuel for RS485 Bus Integrated Controller
Ho原m点e S开wi关tch

4. Negative Origin Mode (PA_040 = 29):After initiating the homing process, the motor moves in the negative
direction at the homing speed (PA_041). When it moves away from the origin switch, the motor decelerates and
stops. It then moves in the positive direction at the homing creep speed (PA_042). When the origin switch is
detected again, the motor stops, completing the homing process.
S开wi关tch

5. Set Current Position as Origin (PA_040 = 35):After initiating the homing process, the current position is
directly set to zero, and a homing complete signal is output.
3.4.3 Control Procedure Description
1. Ensure the default DI port configuration has not been altered;
Parameter No.  Address (Decimal)  Setting Value  Description
| PA_011  |     | 17  | 1   | DI0 configured as origin switch          |     |
| ------- | --- | --- | --- | ---------------------------------------- | --- |
| PA_012  |     | 18  | 2   | DI1 configured as positive limit switch  |     |
| PA_013  |     | 19  | 3   | DI2 configured as negative limit switch  |     |
2. Set the Relevant Homing Parameters: Configure the homing mode (PA_040), homing speed (PA_041), homing creep
speed (PA_042), homing acceleration/deceleration time (PA_043), and homing offset value (PA_044, PA_045).
Once configured, trigger the homing process using Bit4 of the control word (PA_04E) (rising edge). Upon completion of
the homing process, a homing complete signal is output.
3.5 Detailed Parameter Description
3.5.1 Monitoring Parameters
Register Address
| Parameter No.  |     | Item  |     | Description  | Attributes  |
| -------------- | --- | ----- | --- | ------------ | ----------- |
(Decimal)
| PA_001  | 1   | Software Version  |     | Hardware Version  | (RO)  |
| ------- | --- | ----------------- | --- | ----------------- | ----- |
| PA_002  | 2   | Hardware Version  |     | Software Version  | (RO)  |
13

User Manuel for RS485 Bus Integrated Controller
Code  Operating Status
|     |     | Bit0  | In position  |     |     |
| --- | --- | ----- | ------------ | --- | --- |
Bit1  Homing Complete
Bit2  Motor Running
| PA_004  | 4   | Operating Status  |     |        | (RO)  |
| ------- | --- | ----------------- | --- | ------ | ----- |
|         |     | Bit3              |     | Fault  |       |
Bit4  Motor Enabled
Bit5  Positive Soft Limit
Bit6  Negative Soft Limit

Fault Code  Content
|         |     | 0x01           |               | Overcurrent  |       |
| ------- | --- | -------------- | ------------- | ------------ | ----- |
| PA_005  | 5   | Current Alarm  |               |              | (RO)  |
|         |     | 0x02           |               | Overvoltage  |       |
|         |     | 0x03           | Undervoltage  |              |       |

|         |     | Code                      |     | Status  |       |
| ------- | --- | ------------------------- | --- | ------- | ----- |
|         |     | Bit0                      |     | DI0     |       |
|         |     | Bit1                      |     | DI1     |       |
| PA_006  | 6   | DI Group Terminal Status  |     |         | (RO)  |
|         |     | Bit2                      |     | DI2     |       |
|         |     | Bit3                      |     | DI3     |       |
|         |     | Bit4                      |     | DI4     |       |

|         |                              | Code  |     | Status  |       |
| ------- | ---------------------------- | ----- | --- | ------- | ----- |
|         |                              | Bit0  |     | DO0     |       |
| PA_007  | 7  DO Group Terminal Status  |       |     |         | (RO)  |
|         |                              | Bit1  |     | DO1     |       |
|         |                              | Bit2  |     | DO2     |       |

PA_008  8  Current Position H  Open loop for command position,
(RO)
PA_009  9  Current Position L  closed loop for feedback position;
| PA_00A  | 10  | Current Speed  | Unit: r/min  |     | (RO)  |
| ------- | --- | -------------- | ------------ | --- | ----- |
3.5.2 DI/DO Parameters
Register
| Parameter  |          |       |              |     | Setting  |
| ---------- | -------- | ----- | ------------ | --- | -------- |
|            | Address  | Item  | Description  |     |          |
| No.        |          |       |              |     | Range    |
(Decimal)
|     |     |     | Code  | Status  |     |
| --- | --- | --- | ----- | ------- | --- |
|     |     |     | Bit0  | DI0     |     |
|     |     |     | Bit1  | DI1     |     |
DI terminal normally open/closed
| PA_010  | 16  |     | Bit2  | DI2  | 0 ~ 127  |
| ------- | --- | --- | ----- | ---- | -------- |
switching
|     |     |     | Bit3  | DI3  |     |
| --- | --- | --- | ----- | ---- | --- |
|     |     |     | Bit4  | DI4  |     |
0: Normally Open; 1: Normally Closed
|         |     | Code             |            | Function  |         |
| ------- | --- | ---------------- | ---------- | --------- | ------- |
| PA_011  | 17  | DI Input Port 0  |            |           | 0 ~ 17  |
|         |     | 0x00             | Undefined  |           |         |
0x01  Homing signal
0x02  Positive limit
| PA_012  | 18  | DI Input Port 1  |     |     | 0 ~ 17  |
| ------- | --- | ---------------- | --- | --- | ------- |
0x03  Negative limit
14

User Manuel for RS485 Bus Integrated Controller
|         |     |     |     |                  |     | 0x04                         | Release signal  |     |         |
| ------- | --- | --- | --- | ---------------- | --- | ---------------------------- | --------------- | --- | ------- |
| PA_013  | 19  |     |     | DI Input Port 2  |     |                              |                 |     | 0 ~ 17  |
|         |     |     |     |                  |     | 0x05                         | Stop signal     |     |         |
|         |     |     |     |                  |     | 0x06  Forced emergency stop  |                 |     |         |
|         |     |     |     |                  |     | 0x09                         | Positive JOG    |     |         |
| PA_014  | 20  |     |     | DI Input Port 3  |     |                              |                 |     | 0 ~ 17  |
|         |     |     |     |                  |     | 0x0A                         | Negative JOG    |     |         |
|         |     |     |     |                  |     | 0x0B  Homing trigger         |                 |     |         |
|         |     |     |     |                  |     | 0x0C  Position path trigger  |                 |     |         |
|         |     |     |     |                  |     | 0x0D  Speed path trigger     |                 |     |         |
|         |     |     |     |                  |     | 0x0E                         | Path address 0  |     |         |
| PA_015  | 21  |     |     | DI Input Port 4  |     |                              |                 |     | 0 ~ 17  |
|         |     |     |     |                  |     | 0x0F                         | Path address 1  |     |         |
|         |     |     |     |                  |     | 0x10                         | Path address 2  |     |         |
|         |     |     |     |                  |     | 0x11                         | Path address 3  |     |         |
|         |     |     |     |                  |     |                              |                 |     | 0～1024  |
PA_01A  26  Input port filter coefficient  Input port filt er coefficient
|         |     |                                   |     |            |     | Code  | Status  |     |      |
| ------- | --- | --------------------------------- | --- | ---------- | --- | ----- | ------- | --- | ---- |
|         |     | DO terminal normally open/closed  |     |            |     | Bit0  | DO0     |     |      |
| PA_01B  | 27  |                                   |     |            |     |       |         |     | 0~7  |
|         |     |                                   |     | switching  |     | Bit1  | DO1     |     |      |
0: Normally Open; 1: Normally Closed
|         |     |     |     |                   |       | Code              | Function            |     |      |
| ------- | --- | --- | --- | ----------------- | ----- | ----------------- | ------------------- | --- | ---- |
| PA_01C  | 28  |     |     | DO Output Port 0  |       | 0x00              | Undefined           |     | 0~3  |
|         |     |     |     |                   |       | 0x01              | Alarm output        |     |      |
|         |     |     |     |                   |       | 0x02              | Motor Running       |     |      |
|         |     |     |     |                   |       | 0x03              | Homing Complete     |     |      |
| PA_01D  | 29  |     |     | DO Output Port 1  |       |                   |                     |     | 0~3  |
|         |     |     |     |                   |       | 0x04              | In-position signal  |     |      |
|         |     |     |     |                   |       | 0x05              | Brake signal        |     |      |
|         |     |     |     |                   | Code  | DO function code  |                     |     |      |
|         |     |     |     |                   |       | Bit0              | 0x09                |     |      |
|         |     |     |     |                   |       | Bit1              | 0x0A                |     |      |
0: Normally Open; 1: Normally Closed
| PA_01F  | 31  |     | Force output of the output port  |     |     |     |     |     | 0~7  |
| ------- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | ---- |
Note: The output port function must be
set according to the corresponding
function code. The output will only
occur when the corresponding bit is
connected.
3.5.3 Communication Control Parameters
Register
Parameter
|     | Address  |     |     | Item  |     | Description  |     | Setting Range  |     |
| --- | -------- | --- | --- | ----- | --- | ------------ | --- | -------------- | --- |
No.
(Decimal)
| PA_020  | 32  |     |     | 485 ID  | Custom station number  |     |     |     | 0 ~ 254  |
| ------- | --- | --- | --- | ------- | ---------------------- | --- | --- | --- | -------- |
0: 8-bit data, no parity, 1 stop bit; 1: 8-bit
data, no parity, 2 stop bits; 2: 8-bit data,
| PA_021  | 33  | 485 Data Type Selection  |     |     |     |     |     |     | 0~3  |
| ------- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | ---- |
even parity, 1 stop bit; 3: 8-bit data, odd
parity, 1 stop bit
0: Default;
| PA_022  | 34  | Default Direction Setting  |     |     |     |     |     |     | 0~1  |
| ------- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | ---- |
1: Reverse;
PA_023  35  Subdivision Setting  Subdivision Setting  400～51200
0: Stop;
| PA_024  | 36  |     | Limit Stop  |     |     |     |     |     | 0~1  |
| ------- | --- | --- | ----------- | --- | --- | --- | --- | --- | ---- |
1: Forced emergency stop
0: Disabled;
| PA_025  | 37  | Soft Limit Activation  |     |     |     |     |     |     | 0~1  |
| ------- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | ---- |
1: Enabled;
15

User Manuel for RS485 Bus Integrated Controller
Note: Soft limits are only effective after
homing
0: Interrupt current positioning motion to
Internal Multi-Segment
execute new command;
| PA_26  | 38  | Position  |     |     |
| ------ | --- | --------- | --- | --- |
1: Ignore new command if a positioning
 Trigger Mode
motion is in progress
0：115200；
1：38400；
| PA_28  | 40  | RS485 Baud Rate  |     |     |
| ------ | --- | ---------------- | --- | --- |
2：19200；
3：9600；
| PA_030  | 48  | JOG Operating Speed  | Unit: r/min  | -3000～3000  |
| ------- | --- | -------------------- | ------------ | ----------- |
0～2000
| PA_031  | 49  | JOG Acceleration Time          | Unit: ms     |         |
| ------- | --- | ------------------------------ | ------------ | ------- |
| PA_032  | 50  | JOG Deceleration Time          | Unit: ms     | 0～2000  |
| PA_033  | 51  | Positioning Start Speed        | Unit: r/min  | 0～3000  |
| PA_034  | 52  | Positioning Acceleration Time  | Unit: ms     | 0～2000  |
0～2000
| PA_035  | 53  | Positioning Deceleration Time  | Unit: ms     |         |
| ------- | --- | ------------------------------ | ------------ | ------- |
| PA_036  | 54  | Positioning Speed              | Unit: r/min  | 0～3000  |
| PA_037  | 55  | Positioning Target H           |              |         |
-2147483648~
Unit: pulse
2147483647
| PA_038  | 56  | Positioning Target L  |     |     |
| ------- | --- | --------------------- | --- | --- |
17: Negative limit approach;
18: Positive limit approach;
PA_040  64  Homing Mode  24: Positive limit origin approach;  17~35
29: Negative limit origin approach;
35: Current position as origin
| PA_041  | 65  | Homing Approach Speed  | Unit: r/min  | 0～3000  |
| ------- | --- | ---------------------- | ------------ | ------- |
0～3000
| PA_042  | 66  | Homing Creep Speed  | Unit: r/min  |     |
| ------- | --- | ------------------- | ------------ | --- |
Homing Acceleration/
| PA_043  | 67  |     | Unit: ms  | 0～2000  |
| ------- | --- | --- | --------- | ------- |
Deceleration Time
| PA_044  | 68  | Home Offset Value H  |     |     |
| ------- | --- | -------------------- | --- | --- |
-2147483648~
Unit: pulse
2147483647
| PA_045  | 69  | Home Offset Value L    |     |     |
| ------- | --- | ---------------------- | --- | --- |
| PA_046  | 70  | Positive Soft Limit H  |     |     |
-2147483648~
Unit: pulse
| PA_047  | 71  | Positive Soft Limit L  |     | 2147483647  |
| ------- | --- | ---------------------- | --- | ----------- |
| PA_048  | 72  | Negative Soft Limit H  |     |             |
-2147483648~
Unit: pulse
2147483647
| PA_049  | 73  | Negative Soft Limit L  |     |     |
| ------- | --- | ---------------------- | --- | --- |
Internal Multi-Segment
|         |     | Position  0: Relative position mode;                   |     |      |
| ------- | --- | ------------------------------------------------------ | --- | ---- |
| PA_04A  | 74  |                                                        |     | 0~1  |
|         |     | Absolute/Relative Position  1: Absolute position mode  |     |      |
Mode
16

User Manuel for RS485 Bus Integrated Controller
Bit Function Description
Positioning 0: Disabled;
Bit0
Control 1: Enabled;
Positioning 0: Relative;
Bit1
Mode 1: Absolute;
0: Ignore new
command if a
positioning
motion is in
progress
Switch
Bit2 1: Interrupt
Mode
current
PA_04E 78 Control Word positioning 0 ~ 127
motion to
execute new
command;
JOG 0: Disabled;
Bit3
Control 1: Enabled;
Homing 0: Disabled;
Bit4
Control 1: Enabled;
Stop 0: Disabled;
Bit5
Control 1: Enabled;
Emergency
0: Disabled;
Bit6 Stop
1: Enabled;
Control
Code Function
0x0000 N/A
0x0100 Restore Factory
Parameters
0x0200 Save Current
PA_04F 79 Auxiliary Control Parameters
0x0300 Clear Current Alarm
0x0400 Clear Current
Position
0x0500 Motor Enabled
0x0600 Motor Release
3.5.4 Internal Multi-Segment Positioning
Register Address
Parameter No. Item Description Setting Range
(Decimal)
PA_050 80 Position Path 0 Target H -2147483648~
Unit: pulse
PA_051 81 Position Path 0 Target L 2147483647
PA_052 82 Positioning Path 0 Speed Unit: r/min 0～3000
PA_053 83 Positioning Path 0 Acceleration Time Unit: ms 0～2000
PA_054 84 Positioning Path 0 Deceleration Time Unit: ms 0～2000
PA_056 86 Position Path 1 Target H -2147483648~
Unit: pulse
PA_057 87 Position Path 1 Target L 2147483647
PA_058 88 Positioning Path 1 Speed Unit: r/min 0～3000
PA_059 89 Positioning Path 1 Acceleration Time Unit: ms 0～2000
PA_05A 90 Positioning Path 1 Deceleration Time Unit: ms 0～2000
17

User Manuel for RS485 Bus Integrated Controller
| PA_05C  | 92  | Position Path 2 Target H  |     | -2147483648~  |
| ------- | --- | ------------------------- | --- | ------------- |
Unit: pulse
| PA_05D  | 93  | Position Path 2 Target L  |     | 2147483647  |
| ------- | --- | ------------------------- | --- | ----------- |
0～3000
| PA_05E  | 94  | Positioning Path 2 Speed  | Unit: r/min  |     |
| ------- | --- | ------------------------- | ------------ | --- |
PA_05F  95  Positioning Path 2 Acceleration Time  Unit: ms  0～2000
PA_060  96  Positioning Path 2 Deceleration Time  Unit: ms  0～2000
| PA_062  | 98  | Position Path 3 Target H  |     | -2147483648~  |
| ------- | --- | ------------------------- | --- | ------------- |
Unit: pulse
| PA_063  | 99   | Position Path 3 Target L  |              | 2147483647  |
| ------- | ---- | ------------------------- | ------------ | ----------- |
| PA_064  | 100  | Positioning Path 3 Speed  | Unit: r/min  | 0～3000      |
PA_065  101  Positioning Path 3 Acceleration Time  Unit: ms  0～2000
0～2000
| PA_066  | 102  | Positioning Path 3 Deceleration Time  | Unit: ms  |               |
| ------- | ---- | ------------------------------------- | --------- | ------------- |
| PA_068  | 104  | Position Path 4 Target H              |           | -2147483648~  |
Unit: pulse
| PA_069  | 105  | Position Path 4 Target L  |     | 2147483647  |
| ------- | ---- | ------------------------- | --- | ----------- |
0～3000
| PA_06A  | 106  | Positioning Path 4 Speed  | Unit: r/min  |     |
| ------- | ---- | ------------------------- | ------------ | --- |
PA_06B  107  Positioning Path 4 Acceleration Time  Unit: ms  0～2000
PA_06C  108  Positioning Path 4 Deceleration Time  Unit: ms  0～2000
| PA_06E  | 110  | Position Path 5 Target H  |     | -2147483648~  |
| ------- | ---- | ------------------------- | --- | ------------- |
Unit: pulse
| PA_06F  | 111  | Position Path 5 Target L  |              | 2147483647  |
| ------- | ---- | ------------------------- | ------------ | ----------- |
| PA_070  | 112  | Positioning Path 5 Speed  | Unit: r/min  | 0～3000      |
PA_071  113  Positioning Path 5 Acceleration Time  Unit: ms  0～2000
| PA_072  | 114  |     | Unit: ms  | 0～2000  |
| ------- | ---- | --- | --------- | ------- |
Positioning Path 5 Deceleration Time
| PA_074  | 116  | Position Path 6 Target H  |     |     |
| ------- | ---- | ------------------------- | --- | --- |
-2147483648~
Unit: pulse
| PA_075  | 117  | Position Path 6 Target L  |              | 2147483647  |
| ------- | ---- | ------------------------- | ------------ | ----------- |
| PA_076  | 118  |                           | Unit: r/min  | 0～3000      |
Positioning Path 6 Speed
0～2000
| PA_077  | 119  | Positioning Path 6 Acceleration Time  | Unit: ms  |     |
| ------- | ---- | ------------------------------------- | --------- | --- |
PA_078  120  Positioning Path 6 Deceleration Time  Unit: ms  0～2000
| PA_07A  | 122  | Position Path 7 Target H  |     | -2147483648~  |
| ------- | ---- | ------------------------- | --- | ------------- |
Unit: pulse
| PA_07B  | 123  | Position Path 7 Target L  |              | 2147483647  |
| ------- | ---- | ------------------------- | ------------ | ----------- |
| PA_07C  | 124  | Positioning Path 7 Speed  | Unit: r/min  | 0～3000      |
PA_07D  125  Positioning Path 7 Acceleration Time  Unit: ms  0～2000
| PA_07E  | 126  |     | Unit: ms  | 0～2000  |
| ------- | ---- | --- | --------- | ------- |
Positioning Path 7 Deceleration Time
| PA_080  | 128  | Position Path 8 Target H  |     | -2147483648~  |
| ------- | ---- | ------------------------- | --- | ------------- |
Unit: pulse
| PA_081  | 129  | Position Path 8 Target L  |              | 2147483647  |
| ------- | ---- | ------------------------- | ------------ | ----------- |
| PA_082  | 130  |                           | Unit: r/min  | 0～3000      |
Positioning Path 8 Speed
0～2000
| PA_083  | 131  | Positioning Path 8 Acceleration Time  | Unit: ms  |     |
| ------- | ---- | ------------------------------------- | --------- | --- |
PA_084  132  Positioning Path 8 Deceleration Time  Unit: ms  0～2000
| PA_086  | 134  | Position Path 9 Target H  |     | -2147483648~  |
| ------- | ---- | ------------------------- | --- | ------------- |
Unit: pulse
| PA_087  | 135  | Position Path 9 Target L  |              | 2147483647  |
| ------- | ---- | ------------------------- | ------------ | ----------- |
| PA_088  | 136  | Positioning Path 9 Speed  | Unit: r/min  | 0～3000      |
PA_089  137  Positioning Path 9 Acceleration Time  Unit: ms  0～2000
PA_08A  138  Positioning Path 9 Deceleration Time  Unit: ms  0～2000
| PA_08C  | 140  | Position Path 10 Target H  |     | -2147483648~  |
| ------- | ---- | -------------------------- | --- | ------------- |
Unit: pulse
| PA_08D  | 141  | Position Path 10 Target L  |              | 2147483647  |
| ------- | ---- | -------------------------- | ------------ | ----------- |
| PA_08E  | 142  | Positioning Path 10 Speed  | Unit: r/min  | 0～3000      |
| PA_08F  | 143  |                            | Unit: ms     | 0～2000      |
Positioning Path 10 Acceleration Time
PA_090  144  Positioning Path 10 Deceleration Time  Unit: ms  0～2000
| PA_092  | 146  | Position Path 11 Target H  |     | -2147483648~  |
| ------- | ---- | -------------------------- | --- | ------------- |
Unit: pulse
| PA_093  | 147  | Position Path 11 Target L  |     | 2147483647  |
| ------- | ---- | -------------------------- | --- | ----------- |
18

User Manuel for RS485 Bus Integrated Controller
| PA_094  | 148  | Positioning Path 11 Speed  |     | Unit: r/min  | 0～3000  |
| ------- | ---- | -------------------------- | --- | ------------ | ------- |
PA_095  149  Positioning Path 11 Acceleration Time  Unit: ms  0～2000
| PA_096  | 150  |     |     | Unit: ms  | 0～2000  |
| ------- | ---- | --- | --- | --------- | ------- |
Positioning Path 11 Deceleration Time
| PA_098  | 152  | Position Path 12 Target H  |     |     | -2147483648~  |
| ------- | ---- | -------------------------- | --- | --- | ------------- |
Unit: pulse
| PA_099  | 153  | Position Path 12 Target L  |     |              | 2147483647  |
| ------- | ---- | -------------------------- | --- | ------------ | ----------- |
| PA_09A  | 154  | Positioning Path 12 Speed  |     | Unit: r/min  | 0～3000      |
0～2000
PA_09B  155  Positioning Path 12 Acceleration Time  Unit: ms
PA_09C  156  Positioning Path 12 Deceleration Time  Unit: ms  0～2000
| PA_09E  | 158  | Position Path 13 Target H  |     |     | -2147483648~  |
| ------- | ---- | -------------------------- | --- | --- | ------------- |
Unit: pulse
| PA_09F  | 159  | Position Path 13 Target L  |     |              | 2147483647  |
| ------- | ---- | -------------------------- | --- | ------------ | ----------- |
| PA_0A0  | 160  | Positioning Path 13 Speed  |     | Unit: r/min  | 0～3000      |
PA_0A1  161  Positioning Path 13 Acceleration Time  Unit: ms  0～2000
PA_0A2  162  Positioning Path 13 Deceleration Time  Unit: ms  0～2000
| PA_0A4  | 164  | Position Path 14 Target H  |     |     | -2147483648~  |
| ------- | ---- | -------------------------- | --- | --- | ------------- |
Unit: pulse
| PA_0A5  | 165  | Position Path 14 Target L  |     |              | 2147483647  |
| ------- | ---- | -------------------------- | --- | ------------ | ----------- |
| PA_0A6  | 166  | Positioning Path 14 Speed  |     | Unit: r/min  | 0～3000      |
| PA_0A7  | 167  |                            |     | Unit: ms     | 0～2000      |
Positioning Path 14 Acceleration Time
PA_0A8  168  Positioning Path 14 Deceleration Time  Unit: ms  0～2000
| PA_0AA  | 170  | Position Path 15 Target H  |     |     | -2147483648~  |
| ------- | ---- | -------------------------- | --- | --- | ------------- |
Unit: pulse
| PA_0AB  | 171  | Position Path 15 Target L  |     |     | 2147483647  |
| ------- | ---- | -------------------------- | --- | --- | ----------- |
0～3000
| PA_0AC  | 172  | Positioning Path 15 Speed  |     | Unit: r/min  |     |
| ------- | ---- | -------------------------- | --- | ------------ | --- |
PA_0AD  173  Positioning Path 15 Acceleration Time  Unit: ms  0～2000
PA_0AE  174  Positioning Path 15 Deceleration Time  Unit: ms  0～2000
3.5.5 Internal Multi-Segment Speed
Register Address
| Parameter No.  |     |     | Item  | Description  | Setting Range  |
| -------------- | --- | --- | ----- | ------------ | -------------- |
(Decimal)
-3000～3000
| PA_0B0  | 176  | Speed Path 0 Running Speed  |     | Unit: r/min  |     |
| ------- | ---- | --------------------------- | --- | ------------ | --- |
PA_0B1  177  Speed Path 0 Acceleration Time  Unit: ms  0～2000
PA_0B2  178  Speed Path 0 Deceleration Time  Unit: ms  0～2000
PA_0B3  179  Speed Path 1 Running Speed  Unit: r/min  -3000～3000
0～2000
| PA_0B4  | 180  | Speed Path 1 Acceleration Time  |     | Unit: ms  |     |
| ------- | ---- | ------------------------------- | --- | --------- | --- |
PA_0B5  181  Speed Path 1 Deceleration Time  Unit: ms  0～2000
PA_0B6  182  Speed Path 2 Running Speed  Unit: r/min  -3000～3000
PA_0B7  183  Speed Path 2 Acceleration Time  Unit: ms  0～2000
PA_0B8  184  Speed Path 2 Deceleration Time  Unit: ms  0～2000
PA_0B9  185  Speed Path 3 Running Speed  Unit: r/min  -3000～3000
PA_0BA  186  Speed Path 3 Acceleration Time  Unit: ms  0～2000
PA_0BB  187  Speed Path 3 Deceleration Time  Unit: ms  0～2000
PA_0BC  188  Speed Path 4 Running Speed  Unit: r/min  -3000～3000
0～2000
| PA_0BD  | 189  | Speed Path 4 Acceleration Time  |     | Unit: ms  |     |
| ------- | ---- | ------------------------------- | --- | --------- | --- |
PA_0BE  190  Speed Path 4 Deceleration Time  Unit: ms  0～2000
PA_0BF  191  Speed Path 5 Running Speed  Unit: r/min  -3000～3000
PA_0C0  192  Speed Path 5 Acceleration Time  Unit: ms  0～2000
0～2000
| PA_0C1  | 193  | Speed Path 5 Deceleration Time  |     | Unit: ms  |     |
| ------- | ---- | ------------------------------- | --- | --------- | --- |
PA_0C2  194  Speed Path 6 Running Speed  Unit: r/min  -3000～3000
19

User Manuel for RS485 Bus Integrated Controller
PA_0C3  195  Speed Path 6 Acceleration Time  Unit: ms  0～2000
PA_0C4  196  Speed Path 6 Deceleration Time  Unit: ms  0～2000
PA_0C5  197  Speed Path 7 Running Speed  Unit: r/min  -3000～3000
0～2000
| PA_0C6  | 198  | Speed Path 7 Acceleration Time  |     | Unit: ms  |     |
| ------- | ---- | ------------------------------- | --- | --------- | --- |
PA_0C7  199  Speed Path 7 Deceleration Time  Unit: ms  0～2000
PA_0C8  200  Speed Path 8 Running Speed  Unit: r/min  -3000～3000
PA_0C9  201  Speed Path 8 Acceleration Time  Unit: ms  0～2000
PA_0CA  202  Speed Path 8 Deceleration Time  Unit: ms  0～2000
PA_0CB  203  Speed Path 9 Running Speed  Unit: r/min  -3000～3000
PA_0CC  204  Speed Path 9 Acceleration Time  Unit: ms  0～2000
PA_0CD  205  Speed Path 9 Deceleration Time  Unit: ms  0～2000
PA_0CE  206  Speed Path 10 Running Speed  Unit: r/min  -3000～3000
0～2000
| PA_0CF  | 207  | Speed Path 10 Acceleration Time  |     | Unit: ms  |     |
| ------- | ---- | -------------------------------- | --- | --------- | --- |
PA_0D0  208  Speed Path 10 Deceleration Time  Unit: ms  0～2000
PA_0D1  209  Speed Path 11 Running Speed  Unit: r/min  -3000～3000
PA_0D2  210  Speed Path 11 Acceleration Time  Unit: ms  0～2000
0～2000
| PA_0D3  | 211  | Speed Path 11 Deceleration Time  |     | Unit: ms  |     |
| ------- | ---- | -------------------------------- | --- | --------- | --- |
PA_0D4  212  Speed Path 12 Running Speed  Unit: r/min  -3000～3000
PA_0D5  213  Speed Path 12 Acceleration Time  Unit: ms  0～2000
PA_0D6  214  Speed Path 12 Deceleration Time  Unit: ms  0～2000
-3000～3000
| PA_0D7  | 215  | Speed Path 13 Running Speed  |     | Unit: r/min  |     |
| ------- | ---- | ---------------------------- | --- | ------------ | --- |
PA_0D8  216  Speed Path 13 Acceleration Time  Unit: ms  0～2000
PA_0D9  217  Speed Path 13 Deceleration Time  Unit: ms  0～2000
PA_0DA  218  Speed Path 14 Running Speed  Unit: r/min  -3000～3000
PA_0DB  219  Speed Path 14 Acceleration Time  Unit: ms  0～2000
0～2000
| PA_0DC  | 220  | Speed Path 14 Deceleration Time  |     | Unit: ms  |     |
| ------- | ---- | -------------------------------- | --- | --------- | --- |
PA_0DD  221  Speed Path 15 Running Speed  Unit: r/min  -3000～3000
PA_0DE  222  Speed Path 15 Acceleration Time  Unit: ms  0～2000
PA_0DF  223  Speed Path 15 Deceleration Time  Unit: ms  0～2000
3.5.6 Manufacturer Parameters
| Register Address  |            |                            |       |                     | Setting  |
| ----------------- | ---------- | -------------------------- | ----- | ------------------- | -------- |
| Parameter No.     |            |                            | Item  | Description         |          |
|                   | (Decimal)  |                            |       |                     | Range    |
|                   |            | Operating Mode             |       | 1: Open-loop;       |          |
| PA_100            | 256        |                            |       |                     | 1~2      |
|                   |            | (Effective after restart)  |       |  2: Closed-loop;    |          |
| PA_101            | 257        | Encoder Resolution         |       | Encoder Resolution  |          |
Maximum current output by the
| PA_102  | 258  | Maximum Effective Current  |     |     |     |
| ------- | ---- | -------------------------- | --- | --- | --- |
driver, unit: mA;
PA_103  259  Closed loop maximum current ratio  Closed loop maximum current ratio
| PA_104  | 260  | Base current ratio  |     | Base current ratio  |     |
| ------- | ---- | ------------------- | --- | ------------------- | --- |
PA_105  261  Open loop maximum current ratio  Open loop maximum current ratio
| PA_106  | 262  | Lock current ratio  |     | Lock current ratio  |     |
| ------- | ---- | ------------------- | --- | ------------------- | --- |
| PA_107  | 263  | Lock Motor Time     |     | Lock Motor Time     |     |
PA_109  265  Low-pass filter coefficient  Low-pass filter coefficient
PA_10A  266  Position error threshold  Position error threshold
PA_10B  267  Positioning accuracy threshold  Positioning accuracy threshold
20

User Manuel for RS485 Bus Integrated Controller
PA_10C  268  Positioning completion time  Positioning completion time
PA_10D  269  Average filter coefficient  Average filter coefficient
PA_10E  270  Current loop gain adjustment ratio  Current loop gain adjustment ratio
| PA_10F  | 271  | Current Loop Kp       | Current Loop Kp       |     |
| ------- | ---- | --------------------- | --------------------- | --- |
| PA_110  | 272  | Current Loop Ki       | Current Loop Ki       |     |
| PA_111  | 273  | Current Loop Kc       | Current Loop Kc       |     |
| PA_112  | 274  | LA Speed Kp1          | LA Speed Kp1          |     |
| PA_113  | 275  | LA Speed Kv1          | LA Speed Kv1          |     |
| PA_114  | 276  | Speed node 1          | Speed node 1          |     |
| PA_115  | 277  | LA Speed Kp2          | LA Speed Kp2          |     |
| PA_116  | 278  | LA Speed Kv2          | LA Speed Kv2          |     |
| PA_117  | 279  | Speed node 2          | Speed node 1          |     |
| PA_118  | 280  | Speed feedforward     | Speed feedforward     |     |
| PA_119  | 281  | Position integration  | Position integration  |     |

3.6 Alarm Handling
The alarm information for this series of drivers can be identified by the number of times the indicator light blinks.
The specific alarm information is as follows:
| Indicator Light  | Alarm  |     |     |     |
| ---------------- | ------ | --- | --- | --- |
Troubleshooting  Reset
| Blinking Frequency  | Description  |     |     |     |
| ------------------- | ------------ | --- | --- | --- |
1.  Motor wiring short circuit, check motor wiring;
Blinks once every 5  2.  Motor damage, measure the resistance of the motor's  Restart to
Overcurrent Alarm
| seconds  |     | A-phase and B-phase windings;  |     | reset  |
| -------- | --- | ------------------------------ | --- | ------ |
3.  Driver damage, replace the driver.
1.  Power supply voltage is too high, measure the power
| Blinks twice every 2  |                    |                                              |     | Restart to  |
| --------------------- | ------------------ | -------------------------------------------- | --- | ----------- |
|                       | Overvoltage Alarm  | supply voltage or replace the power supply;  |     |             |
| seconds               |                    |                                              |     | reset       |
2.  Driver damage, replace the driver.
1.  Power supply voltage is too low, measure the power
| Blinks three times  | Undervoltage  |     |     | Restart to  |
| ------------------- | ------------- | --- | --- | ----------- |
supply voltage or replace the power supply;
| every 5 seconds  | Alarm  |     |     | reset  |
| ---------------- | ------ | --- | --- | ------ |
2.  Driver damage, replace the driver.
| Blinks 4 times every  | Memory            |                                            |     |               |
| --------------------- | ----------------- | ------------------------------------------ | --- | ------------- |
|                       |                   | Driver damage, please replace the driver.  |     | Can be reset  |
| 5 seconds             | Read/Write Error  |                                            |     |               |
1.  Motor power line phase sequence error, check wiring
sequence;
2.  Motor line phase loss, check if the wire is broken or
| Blinks five times  | Position Error  |                    |     |               |
| ------------------ | --------------- | ------------------ | --- | ------------- |
|                    |                 | has poor contact;  |     | Can be reset  |
every 5 seconds  Alarm
3.  Encoder line disconnection;
4.  Load jam;
5.  Speed too fast.

Chapter 4: MODBUS RTU Instructions
4.1 Read Parameter Command (0x03)
Master (e.g., PLC) Sends the Command:
21

User Manuel for RS485 Bus Integrated Controller
| Byte Order  | Example  | Symbol  | Function  |     |
| ----------- | -------- | ------- | --------- | --- |
Command
| 1st Byte  | 0x01  | Slave Addr  | Slave address, here it is 1  |     |
| --------- | ----- | ----------- | ---------------------------- | --- |
2nd Byte  0x03  CMD  Function code, here 0x03, indicating a read parameter command
3rd Byte  0x00  Start AddrH  High 8 bits of the starting address of the parameter to be read
4th Byte  0x0A  Start AddrL  Low 8 bits of the starting address of the parameter to be read
5th Byte  0x00  Num_ High(Byte)  High 8 bits of the number of parameters to read (in words, not
bytes)
6th Byte  0x01  Num_Low(Byte)  High 8 bits of the number of parameters to read
7th Byte  0Xa4  CRC_H  High byte of the CRC check (CRC check is done on bytes 1
through 6)
| 8th Byte  | 0x08  | CRC_L  | Low byte of the CRC check  |     |
| --------- | ----- | ------ | -------------------------- | --- |
[Example: The master reads one parameter (2 bytes) from the slave at address 1, starting from address 10 (0x000A)]
Slave (Driver) Responds:
| Byte Order  | Example  | Symbol  | Function  |     |
| ----------- | -------- | ------- | --------- | --- |
Command
| 1st Byte  | 0x01  | Slave Addr  | Slave address, here it is 1  |     |
| --------- | ----- | ----------- | ---------------------------- | --- |
2nd Byte  0x03  CMD  Function code, 0x03, corresponding to the master command
3rd Byte  0x02  Data Lenth  Length of the response data, in bytes
4th Byte  0x00  Data0  Data0 (High byte of the first register)
5th Byte  0x00  Data0  Data0 (Low byte of the first register)
6th Byte  0Xb8  CRC_H  High byte of the CRC check (CRC check is done on bytes 1 through 9)
| 7th Byte  | 0x44  | CRC_L  | Low byte of the CRC check  |     |
| --------- | ----- | ------ | -------------------------- | --- |
[Response Data0: 0x0000]
4.2 Write to a single register (0x06)
Master (e.g., PLC) Sends the Command:
| Byte Order  | Example  | Symbol  |     |     |
| ----------- | -------- | ------- | --- | --- |
Function
Command
| 1st Byte  | 0x01  | Slave Addr  | Slave address, here it is 1  |     |
| --------- | ----- | ----------- | ---------------------------- | --- |
2nd Byte  0x06  CMD  Function code, here 0x06, indicating a write single parameter command
3rd Byte  0x00  Start AddrH  High 8 bits of the starting address of the parameter to be written
4th Byte  0x70  Start AddrL  Low 8 bits of the starting address of the parameter to be written
5th Byte  0x00  DATA(0)  High 8 bits of the data to be written
6th Byte  0x14  DATA(1)  Low 8 bits of the data to be written
7th Byte  0x88  CRC_H  High byte of the CRC check (CRC check is done on bytes 1 through 6)
| 8th Byte  | 0x1E  | CRC_L  | Low byte of the CRC check  |     |
| --------- | ----- | ------ | -------------------------- | --- |
[Example: The master writes a value of 20 (0x0014) to the slave at address 1, starting from address 112 (0x0070)]

Slave (Driver) Responds:
Example
| Byte Order  |     | Symbol  |     | Function  |
| ----------- | --- | ------- | --- | --------- |
Command
| 1st Byte  | 0x01  | Slave Addr  | Slave address, here it is 1  |     |
| --------- | ----- | ----------- | ---------------------------- | --- |
2nd Byte  0x06  CMD  Function code, 0x06, corresponding to the master command
3rd Byte  0x00  Start AddrH  High 8 bits of the starting address of the written parameter
4th Byte  0x70  Start AddrL  Low 8 bits of the starting address of the written parameter
| 5th Byte  | 0x00  | DATA(0)  | High 8 bits of the written data  |     |
| --------- | ----- | -------- | -------------------------------- | --- |
| 6th Byte  | 0x14  | DATA(1)  | Low 8 bits of the written data   |     |
High byte of the CRC check (CRC check is done on bytes 1
| 7th Byte  | 0x88  | CRC_H  |     |     |
| --------- | ----- | ------ | --- | --- |
through 6)
| 8th Byte  | 0x1E  | CRC_L  | Low byte of the CRC check  |     |
| --------- | ----- | ------ | -------------------------- | --- |
22

User Manuel for RS485 Bus Integrated Controller
4.3 Write Multiple Registers Command (0x10)
Master (e.g., PLC) Sends the Command:
Example
| Byte Order  |     | Symbol  |     | Function  |
| ----------- | --- | ------- | --- | --------- |
Command
| 1st Byte  | 0x01  | Slave Addr  | Slave address, here it is 1  |     |
| --------- | ----- | ----------- | ---------------------------- | --- |
Function code, here 0x10, indicating a write multiple parameters
| 2nd Byte  | 0x10  | CMD  |     |     |
| --------- | ----- | ---- | --- | --- |
command
3rd Byte  0x00  Start AddrH  High 8 bits of the starting address of the parameter to be written
4th Byte  0xB0  Start AddrL  Low 8 bits of the starting address of the parameter to be written
5th Byte  0x00  NUM_H  High 8 bits of the number of parameters (registers) to be written
6th Byte  0x02  NUM_L  Low 8 bits of the number of parameters (registers) to be written
7th Byte  0x04  Data Lenth  Length of the data to be written, which is twice the number of registers
8th Byte  0x03  DATA(0)  High 8 bits of the first data to be written
9th Byte  0xE8  DATA(0)  Low 8 bits of the first data to be written
10th Byte  0x00  DATA(1)  High 8 bits of the second data to be written
11th Byte  0x64  DATA(1)  Low 8 bits of the second data to be written
12th Byte  0x79  CRC_H  High byte of the CRC check (CRC check is done on bytes 1 through 6)
| 13th Byte  | 0x40  | CRC_L  | Low byte of the CRC check  |     |
| ---------- | ----- | ------ | -------------------------- | --- |
[Example: The master writes two parameters to the slave at address 1, starting from address 176 (0x00B0):
176(0x00B0)=1000(0x03E8)、177(0x00B1)=100(0x0064)]

Slave (Driver) Responds:
Example
| Byte Order  |     | Symbol  |     | Function  |
| ----------- | --- | ------- | --- | --------- |
Command
| 1st Byte  | 0x01  | Slave Addr  | Slave address, here it is 1  |     |
| --------- | ----- | ----------- | ---------------------------- | --- |
2nd Byte  0x10  CMD  Function code, 0x10, corresponding to the master command
3rd Byte  0x00  Start AddrH  High 8 bits of the starting address of the written parameter
4th Byte  0xB0  Start AddrL  Low 8 bits of the starting address of the written parameter
5th Byte  0x00  NUM_H  High 8 bits of the number of parameters (registers) written
6th Byte  0x02  NUM_L  Low 8 bits of the number of parameters (registers) written
7th Byte  0x40  CRC_H  High byte of the CRC check (CRC check is done on bytes 1 through 6)
| 8th Byte  | 0x2F  | CRC_L  | Low byte of the CRC check  |     |
| --------- | ----- | ------ | -------------------------- | --- |
4.4 Exception Responses and Error Codes
When a slave encounters an exception while processing a read or write command, its response frame will change as follows:
| Byte      | Example  |             |                              |           |
| --------- | -------- | ----------- | ---------------------------- | --------- |
|           |          | Symbol      |                              | Function  |
| Order     | Command  |             |                              |           |
| 1st Byte  | 0x01     | Slave Addr  | Slave address, here it is 1  |           |
2nd Byte  0x06  CMD|0x80  The highest bit of the function code is set to 1
Error code indicating the type of error encountered:
0x02: Illegal address
| 3rd Byte  | 0x04  | Error Code  |     |     |
| --------- | ----- | ----------- | --- | --- |
0x03: Illegal data
0x04: Execution denied
High byte of the CRC check High byte of the CRC check (CRC check is
| 4th Byte  | 0x10  | CRC_H  |     |     |
| --------- | ----- | ------ | --- | --- |
done on bytes 1 through 3)
| 5th Byte  | 0x00  | CRC_L  | Low byte of the CRC check  |     |
| --------- | ----- | ------ | -------------------------- | --- |

23