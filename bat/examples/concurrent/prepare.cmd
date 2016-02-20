
for /L %%i in (1,1,3) do (
    md %%i-suite
    copy LongTaskTemplate.cmd %%i-suite
)

for /L %%i in (1,1,3) do (
    md %%i
    copy LongTaskTemplate.cmd %%i
)