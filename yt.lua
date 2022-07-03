-- Tested in CC: Restitched
-- Script to download a song from the API and play it through the speaker

local api = "" -- EDIT ME

local args = { ... }

if #args ~= 1 then
    error("Usage: yt <video id>")
end

-- Download
shell.run("wget", api .. args[1])

-- Play
local speaker = peripheral.find("speaker")
local dfpwm = require("cc.audio.dfpwm")
local decoder = dfpwm.make_decoder()

for chunk in io.lines(args[1], 16 * 1024) do
    local buffer = decoder(chunk)

    while not speaker.playAudio(buffer) do
        os.pullEvent("speaker_audio_empty")
    end
end

-- Delete file
shell.run("rm", args[1])