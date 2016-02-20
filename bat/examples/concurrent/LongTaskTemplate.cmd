cd %1
for /L %%i in (1,1,800) do (
 md test-%%i
)
exit 0