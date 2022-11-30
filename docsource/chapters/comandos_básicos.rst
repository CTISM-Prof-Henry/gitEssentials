.. _comandos-basicos:

Comandos Básicos
================

Uma vez que um repositório é clonado, precisaremos (na maioria das vezes) de um conjunto restrito de comandos para
trabalhar localmente.

Os fluxogramas desta seção foram adaptados do material do material de Fabrício Cabral no seu repositório
`gitflowchart <https://github.com/fabriciofx/gitflowchart>`__.

.. graphviz::

    digraph commonworkflow {
        splines = ortho;
        overlap = false;

        edge [
            arrowsize = 0.8,
            fontname = "Verdana",
            fontsize = 12
        ]

        node [
            shape = rect,
            style = filled,
            fillcolor = lightyellow,
            fontname = "Verdana",
            fontsize = 12
        ]

        // dot
        dot1 [
            shape = point,
            style = invis,
            width = 0,
            group = right
        ]
        dot2 [
            shape = point,
            style = invis,
            width = 0,
            group = right
        ]

        // workflow
        common_workflow [
            shape = invhouse,
            label = <<b>Common<br/>workflow</b>>,
            group = main
        ]
        sharing_workflow [
            shape = invhouse,
            label = <<b>Sharing<br/>workflow</b>>,
            group = main
        ]

        // actions
        create_new_files_or_edit_existent_files [
            label = <<b>Create new or edit<br/>existent files</b>>,
            group = main
        ]

        // decisions
        check_what_will_be_commited [
            shape = diamond,
            label = <<b>Check what<br/>will be<br/>commited?</b>>,
            height = 1,
            group = main
        ]
        fine_to_commit [
            shape = diamond,
            label = <<b>Fine to<br/>commit?</b>>,
            height = 1,
            group = main
        ]
        would_you_like_share_the_changes [
            shape = diamond,
            label = <<b>Would you<br/>like share<br/>the changes?</b>>,
            height = 1,
            group = main
        ]

        // commands
        git_add [
            label = <
                <table border="0" cellborder="0" cellspacing="0">
                <tr><td><b>Put the changes into staging area</b></td></tr>
                <tr><td>git add .</td></tr>
                </table>
            >,
            group = main
        ]
        git_status [
            label = <
                <table border="0" cellborder="0" cellspacing="0">
                <tr><td><b>Check the content to commit</b></td></tr>
                <tr><td>git status</td></tr>
                </table>
            >,
            group = main
        ]
        git_commit [
            label = <
                <table border="0" cellborder="0" cellspacing="0">
                <tr><td><b>Create the commit</b></td></tr>
                <tr><td>git commit -m "message"</td></tr>
                </table>
            >,
            group = main
        ]
        git_restore [
            label = <
                <table border="0" cellborder="0" cellspacing="0">
                <tr><td><b>Restore from staging area</b></td></tr>
                <tr><td>git restore --staged &lt;filename&gt;</td></tr>
                </table>
            >
        ]

        // relations
        common_workflow -> create_new_files_or_edit_existent_files
        create_new_files_or_edit_existent_files -> git_add
        git_add -> check_what_will_be_commited
        check_what_will_be_commited -> git_status [label = <<b>   yes</b>>]
        git_status -> fine_to_commit
        fine_to_commit -> git_commit [label = <<b>   yes</b>>]
        git_commit -> would_you_like_share_the_changes
        would_you_like_share_the_changes -> sharing_workflow [label = <<b>   yes</b>>]

        check_what_will_be_commited -> dot1 [dir = none, label = <<b>no</b>>, minlen = 2]
        dot1 -> git_commit

        // left
        git_restore -> git_status [minlen = 2]
        fine_to_commit -> git_restore [xlabel = <<b>no</b>>]

        // right
        would_you_like_share_the_changes -> dot2 [dir = none, label = <<b>no</b>>, minlen = 3]
        create_new_files_or_edit_existent_files -> dot2 [dir = back]

        // put them on the same horizontal line
        { rank = same; check_what_will_be_commited; dot1 }
        { rank = same; would_you_like_share_the_changes; dot2; }
        { rank = same; git_restore; git_status; }
    }