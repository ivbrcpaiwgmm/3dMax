macroScript CreateMyButton category:"My Scripts" buttonText:"My Import" tooltip:"Run My Python Import Script"
(
    rollout MyRollout "My Rollout"
    (
        button btn_import "Import Data" width:100 height:30
        on btn_import pressed do
        (
            local scriptPath = (getDir #scripts) + "\\MyScripts\\import_data.py"
            python.ExecuteFile scriptPath
        )
    )

    createDialog MyRollout
)
