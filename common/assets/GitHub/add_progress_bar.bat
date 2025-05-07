@echo off
set "input=%~1"
set output=%~dpn1_progress_bar.gif

:: Get metadata using ffprobe into temp files
ffprobe -v error -select_streams v:0 -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "%input%" > tmp_duration.txt
ffprobe -v error -select_streams v:0 -show_entries stream=width -of default=noprint_wrappers=1:nokey=1 "%input%" > tmp_width.txt
ffprobe -v error -select_streams v:0 -show_entries stream=height -of default=noprint_wrappers=1:nokey=1 "%input%" > tmp_height.txt

set /p duration=<tmp_duration.txt
set /p width=<tmp_width.txt
set /p height=<tmp_height.txt

del tmp_duration.txt
del tmp_width.txt
del tmp_height.txt

:: Confirm values
echo Duration: %duration%
echo Width: %width%
echo Height: %height%

:: Calculate progress bar height as 5% of input height
set /a barheight=%height%/20

:: Run ffmpeg with dynamic values
ffmpeg -i "%input%" -filter_complex "[0:v]split[base][palettegen];color=c=#FF0000@0.5:s=%width%x%barheight%:d=%duration%,format=rgba[bar];[base][bar]overlay=x='-w+(w/%duration%)*t':y=H-h:shortest=1:format=auto[f];[palettegen]palettegen=stats_mode=full[pal];[f][pal]paletteuse=dither=bayer:bayer_scale=5" "%output%"

echo.
echo Done! Output file: %output%
pause
