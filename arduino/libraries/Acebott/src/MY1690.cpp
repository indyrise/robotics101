#include"MY1690.h"
#include"Arduino.h"

void my1690::play()
{
    byte play[5] = {0x7E,0x03,0x11,0x12,0xEF};
    Serial.write(play,5);
}

void my1690::pause()
{
    byte pause[5] = {0x7E,0x03,0x12,0x11,0xEF};
    Serial.write(pause,5);
}

void my1690::nextTrack()
{
    byte nextTrack[5] = {0x7E,0x03,0x13,0x10,0xEF};
    Serial.write(nextTrack,5);
}

void my1690::previousTrack()
{
    byte previousTrack[5] = {0x7E,0x03,0x14,0x17,0xEF};
    Serial.write(previousTrack,5);
}

void my1690::volunePlus()
{
    byte volunePlus[5] = {0x7E,0x03,0x15,0x16,0xEF};
    Serial.write(volunePlus,5);
}

void my1690::voluneDown()
{
    byte voluneDown[5] = {0x7E,0x03,0x16,0x15,0xEF};
    Serial.write(voluneDown,5);
}

void my1690::reset()
{
    byte reset[5] = {0x7E,0x03,0x19,0x1A,0xEF};
    Serial.write(reset,5);
}

void my1690::fastForward()
{
    byte fastForward[5] = {0x7E,0x03,0x1A,0x19,0xEF};
    Serial.write(fastForward,5);
}

void my1690::fastBackward()
{
    byte fastBackward[5] = {0x7E,0x03,0x1B,0x18,0xEF};
    Serial.write(fastBackward,5);
}

void my1690::playPause()
{
    byte playPause[5] = {0x7E,0x03,0x1C,0x1F,0xEF};
    Serial.write(playPause,5);
}

void my1690::stop()
{
    byte stop[5] = {0x7E,0x03,0x1E,0x1D,0xEF};
    Serial.write(stop,5);
}

void my1690::setVolume()
{
    byte setVolume[6] = {0x7E,0x04,0x31,0x19,0x2C,0xEF};
    Serial.write(setVolume,6);
}

void my1690::setEQ()
{
    byte setEQ[6] = {0x7E,0x04,0x32,0x00,0x36,0xEF};
    Serial.write(setEQ,6);
}

void my1690::setLoopMode()
{
    byte setLoopMode[6] = {0x7E,0x04,0x33,0x00,0x37,0xEF};
    Serial.write(setLoopMode,6);
}

void my1690::folderSwitch()
{
    byte folderSwitch[6] = {0x7E,0x04,0x34,0x01,0x31,0xEF};
    Serial.write(folderSwitch,6);
}

void my1690::selectPlay()
{
    byte selectPlay[7] = {0x7E,0x05,0x41,0x00,0x01,0x45,0xEF};
    Serial.write(selectPlay,7);
}

void my1690::playInFolder()
{
    byte playInFolder[7] = {0x7E,0x05,0x42,0x01,0x01,0x47,0xEF};
    Serial.write(playInFolder,7);
}

void my1690::intercut()
{
    byte intercut[7] = {0x7E,0x05,0x43,0x00,0x03,0x45,0xEF};
    Serial.write(intercut,7);
}

void my1690::intercutToFolder()
{
    byte intercutToFolder[7] = {0x7E,0x05,0x44,0x01,0x06,0x46,0xEF};
    Serial.write(intercutToFolder,7);
}