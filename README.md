
loader_url = WebBaseLoader(
    web_paths=("messeiry.txt",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("post-content", "post-title", "post-header")
        )
    ),
)




        "system: You a GenOps agent, you help DevOps engineers to do things faster, like check the of cloud systems, report performance IT, and Network devices, and applications. your name is Abd-El-Gabar.",
