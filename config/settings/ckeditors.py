CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
    },
}
CKEDITOR_5_CONFIGS = {
    'extends': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link', 'bulletedList',
                    'numberedList', 'blockQuote', 'imageUpload'],
        'image': {
            'toolbar': ['imageTextAlternative', '|',
                        'imageStyle:alignLeft', 'imageStyle:alignRight',
                        'imageStyle:alignCenter', 'imageStyle:side'],
        },
        'heading': {
            'options': [
                {'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph'},
                {'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1'},
                {'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2'},
            ]
        }
    }
}