#!/usr/bin/env python3
"""Generate full course website for ai-perusteet-1ov — Business College Helsinki branding
Completely redesigned with Codecademy-inspired vertical layout, expandable accordions, and paper background."""

import os, json, re
import markdown as md_lib

_HERE = os.path.dirname(os.path.abspath(__file__))
BASE = _HERE
OUT  = os.path.join(_HERE, 'index.html')

# BC Logo: Icon (crest/shield 85x45)
BC_ICON_SVG = '''<svg width="85" height="45" fill="none" xmlns="http://www.w3.org/2000/svg"><g clip-path="url(#clip0_339_29567)"><mask id="a" style="mask-type:luminance" maskUnits="userSpaceOnUse" x="0" y="0" width="85" height="45"><path d="M85 0H0v45h85V0z" fill="#fff"/></mask><g mask="url(#a)" fill="#69013B"><path d="M12.822 11.656c0 2.889-2.158 4.723-5.597 4.723-1.535 0-2.822-.548-3.579-1.53v1.226H.376v-.198l1.266-1.833V2.012L.134.198V0h5.335c3.955 0 5.664 1.135 5.664 3.588 0 1.795-1.468 3.193-3.78 3.655 3.223 0 5.462 1.814 5.462 4.42l.007-.007zM3.686.66v6.47h1.555c2.353 0 4.002-1.2 4.002-3.502 0-2.012-1.22-2.975-3.78-2.975H3.685V.66zm7.024 11.26c0-2.626-1.642-4.136-4.463-4.136H3.693V13.8c.623 1.114 1.843 1.747 3.358 1.747 2.42 0 3.666-1.418 3.666-3.628m4.417.766V9.71c0-1.597-.134-2.381-.845-2.797l2.159-1.049h.51v6.781c0 1.596.69 2.797 2.332 2.797 2.044 0 2.734-1.398 2.734-2.777V9.71c0-1.597-.241-2.362-.931-2.797l2.265-1.049h.49v8.331l.89 1.643v.237h-2.667V14.98c-.49.726-1.18 1.399-2.956 1.399-1.642 0-3.975-.746-3.975-3.693m13.216 3.08l-1.153.462h-.288v-2.955h.51c.509 1.51 1.756 2.493 3.263 2.493 1.602 0 2.312-.765 2.312-1.795 0-2.513-6.133-2.032-6.133-5.602 0-1.728 1.776-2.664 3.733-2.664 1.327 0 2.567.395 3.09 1.048v2.42h-.51c-.422-1.484-1.34-2.903-2.815-2.903-1.34 0-1.843.765-1.843 1.577 0 2.606 6.153 1.966 6.153 5.602 0 1.92-1.562 2.843-3.706 2.843-1.394 0-2.835-.389-3.54-1.2v-2.513h.49c.509 1.596 1.662 3.213 3.397 3.213 1.08 0 2.058-.54 2.058-1.728m6.47-5.594h-1.508v-.257l2.815-1.504h.51v1.728h2.929v.951h-2.93v4.48c0 1.399.383 2.164 1.535 2.164.878 0 1.636-.455 2.232-1.154l.382.257c-.717 1.114-1.843 1.728-3.37 1.728-1.79 0-3.076-.852-3.076-2.71v-4.765h.48zm12.028-3.715l-2.158 1.048c.71.416.844 1.188.844 2.797v4.197c0 1.596.69 2.797 2.332 2.797 2.044 0 2.734-1.398 2.734-2.777V12.74c0-1.597-.241-2.362-.931-2.797l2.265-1.049h.489v8.332l.891 1.642v.237h-2.647v-1.095c-.49.726-1.179 1.399-2.956 1.399-1.642 0-3.974-.746-3.974-3.694v-5.65c0-1.596-.134-2.38-.845-2.796l2.158-1.049h.51v.496h-.712zm10.451 4.223c.711-2.685 2.554-4.223 4.531-4.223.952 0 1.743.284 2.205.818v3.001h-.51c-.382-2.15-1.555-3.253-2.875-3.253-2.286 0-3.352 2.177-3.352 4.526v2.342c0 1.596.69 2.797 2.332 2.797h.201l1.153-.462v.462h-6.06v-.198l1.153-1.663v-5.856c0-1.597-.134-2.381-.845-2.797l2.159-1.049h.489v5.093h-.113zm10.818 5.424l-1.152 1.663v.198h4.088v-.198l-1.113-1.682V6.55c0-1.616-.402-2.361-1.112-2.823L58.362.434h.489V14.59l-.007.001zm1.977-16.184c0 .746-.603 1.345-1.36 1.345-.758 0-1.361-.6-1.361-1.345 0-.746.603-1.345 1.36-1.345.758 0 1.361.6 1.361 1.345M59.3 16.103l1.153-1.663V6.55c0-1.616-.402-2.361-1.113-2.823l-1.247-1.293h.49v6.848c.73-.903 1.997-1.853 3.867-1.853 1.642 0 3.975.745 3.975 3.693v5.857l1.153 1.663v.198h-4.088v-.198l1.112-1.682v-5.59c0-1.597-.69-2.797-2.332-2.797-2.044 0-2.734 1.398-2.734 2.777v5.79l1.112 1.682v.198H59.3v-.198zm14.41-8.56c2.105 0 3.686 1.365 3.686 3.864v.396h-7.037c0 2.289 1.18 4.486 3.6 4.486 1.394 0 2.432-.534 3.15-1.774l.422.178c-.51 1.28-1.843 2.447-3.746 2.447-2.875 0-5.03-2.033-5.03-5.139 0-3.106 2.051-4.925 4.955-4.925zM70.379 11.1h4.957c-.047-2.31-1.313-3.062-2.554-3.062-1.696 0-2.693 1.577-2.403 3.062z"/><path d="M14.06 34.847c0 5.074-3.55 8.24-9.098 8.24-2.486 0-4.576-.879-5.896-2.447v1.86H0v-.33l2.079-3.073V28.48L0 25.166v-.33h8.747c6.43 0 9.2 1.886 9.2 5.963 0 2.98-2.372 5.313-6.163 6.067 5.237 0 8.283 3.006 8.283 7.336l-.007-.355zM2.345 25.98v12.567h2.534c3.816 0 6.494-1.987 6.494-5.81 0-3.338-1.977-4.928-6.14-4.928h-2.89v-1.83zm11.376 18.71c0-4.358-2.661-6.854-7.25-6.854h-4.133v9.976c1.013 1.848 2.993 2.891 5.452 2.891 3.931 0 5.958-2.356 5.958-6.014m4.209-11.678c0-4.345 3.803-6.995 8.266-6.995 4.464 0 8.28 2.98 8.28 8.805 0 5.313-4.006 8.538-8.22 8.538-4.756 0-8.327-3.019-8.327-8.558v-1.79zm14.116.306c0-4.854-2.333-8.222-5.73-8.222-3.21 0-5.237 2.867-5.237 7.36 0 4.993 2.446 8.448 6.06 8.448 2.993 0 4.907-2.943 4.907-7.586m5.49 7.652l1.878-2.753V29.3c0-2.675-.215-3.949-1.368-4.638l3.514-1.742h.798v2.267c1.383-1.58 3.234-2.573 5.77-2.573 2.662 0 6.428 1.235 6.428 6.116v9.774l1.877 2.753v.33h-6.63v-.33l1.8-2.79v-9.49c0-2.65-1.115-4.638-3.778-4.638-3.31 0-4.45 2.318-4.45 4.611v9.556l1.8 2.79v.33h-6.63v-.33h-.01zm20.168 0l1.878-2.753V29.3c0-2.675-.215-3.949-1.368-4.638l3.513-1.742h.799v2.267c1.382-1.58 3.233-2.573 5.77-2.573 2.661 0 6.428 1.235 6.428 6.116v9.774l1.877 2.753v.33h-6.63v-.33l1.8-2.79v-9.49c0-2.65-1.115-4.638-3.778-4.638-3.31 0-4.45 2.318-4.45 4.611v9.556l1.8 2.79v.33h-6.63v-.33h-.009zm18.749 0l1.878-2.753V22.14c0-2.675-.646-3.911-1.8-4.675l-2.016-2.14h.799v23.518l1.8 2.79v.33h-6.63v-.33h-.031zm3.207-26.766c0 1.235-.977 2.229-2.205 2.229a2.222 2.222 0 01-2.206-2.23c0-1.234.977-2.228 2.206-2.228 1.228 0 2.205.994 2.205 2.229m4.59 26.766l1.877-2.753V22.14c0-2.675-.645-3.911-1.8-4.675l-2.015-2.14h.798v11.32c1.18-1.504 3.234-3.072 6.264-3.072 2.662 0 6.429 1.235 6.429 6.116v9.774l1.877 2.753v.33h-6.63v-.33l1.8-2.79v-9.49c0-2.65-1.115-4.638-3.778-4.638-3.31 0-4.45 2.318-4.45 4.611v9.556l1.8 2.79v.33h-6.63v-.33h.458zm23.338-14.152c3.398 0 5.958 2.254 5.958 6.395v.652h-11.383c0 3.772 1.912 7.409 5.82 7.409 2.256 0 3.93-1.031 5.096-2.93l.684.305c-.824 2.114-2.979 4.04-6.06 4.04-4.651 0-8.124-3.364-8.124-8.494 0-5.13 3.323-8.258 8.009-8.258v.88zm-5.425 6.001h7.896c-.076-3.823-2.13-5.07-4.131-5.07-2.74 0-4.373 2.606-3.765 5.07z"/><path d="M16.133 31.537c0-3.476 2.821-5.336 5.53-5.336 2.707 0 5.576 1.814 5.576 5.204 0 3.39-2.755 5.468-5.403 5.468-3.09 0-5.71-1.88-5.71-5.336h.007zm8.927.198c0-2.929-1.44-4.967-3.532-4.967-1.977 0-3.224 1.728-3.224 4.44 0 3.014 1.508 5.092 3.734 5.092 1.843 0 3.022-1.775 3.022-4.572"/><path d="M0 28.536c0-4.345 3.264-7.198 7.198-7.198 4.505 0 7.198 4.505 7.198 8.814 0 4.31-3.264 7.198-7.198 7.198-4.505 0-7.198-4.505-7.198-8.814zm12.353-1.128c0-5.47-2.353-5.815-5.815-5.815-2.353 0-5.815 2.353-5.815 7.198 0 5.47 2.353 12.353 5.815 12.353 2.353 0 5.815-2.353 5.815-12.353v-1.383z" fill-opacity=".01"/></g></g><defs><clipPath id="clip0_339_29567"><path fill="#fff" d="M0 0h85v45H0z"/></clipPath></defs></svg>'''

# BC Logo: Wordmark "Business College Helsinki"
BC_WORDMARK_SVG = '''<svg viewBox="0 0 349 54" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M27.032 25.37c0 6.289-4.598 10.28-11.924 10.28-3.27 0-6.012-1.191-7.625-3.33v2.67H.514v-.43l2.699-3.992V4.379L0 .431V0h11.367c8.425 0 12.067 2.47 12.067 7.81 0 3.906-3.128 6.95-8.054 7.955 6.869 0 11.638 3.948 11.638 9.62l.014-.015zM7.57 1.436V15.52h3.313c5.012 0 8.525-2.613 8.525-7.624 0-4.38-2.6-6.476-8.054-6.476H7.569v.015zm14.965 24.509c0-5.715-3.498-9.003-9.51-9.003H7.583v13.095c1.328 2.426 3.927 3.804 7.154 3.804 5.155 0 7.812-3.087 7.812-7.896m9.411 1.665v-6.475c0-3.475-.286-5.184-1.8-6.088l4.598-2.283h1.085v14.76c0 3.474 1.471 6.088 4.97 6.088 4.355 0 5.826-3.044 5.826-6.045v-6.432c0-3.475-.514-5.14-1.985-6.088l4.827-2.283h1.042v18.134l1.9 3.575v.517h-5.684v-2.384c-1.042 1.58-2.513 3.044-6.297 3.044-3.499 0-8.468-1.622-8.468-8.04m28.16 6.705l-2.456 1.005h-.614v-6.432h1.085c1.086 3.288 3.742 5.427 6.955 5.427 3.413 0 4.927-1.666 4.927-3.905 0-5.47-13.067-4.422-13.067-12.19 0-3.762 3.784-5.8 7.954-5.8 2.827 0 5.469.86 6.583 2.282v5.27h-1.085c-.9-3.231-2.856-6.32-5.998-6.32-2.856 0-3.927 1.666-3.927 3.432 0 5.671 13.11 4.279 13.11 12.19 0 4.18-3.327 6.19-7.897 6.19-2.97 0-6.04-.847-7.54-2.614v-5.47h1.042c1.085 3.474 3.541 6.992 7.24 6.992 2.299 0 4.384-1.177 4.384-3.76m13.781-12.176h-3.213v-.56l5.997-3.273h1.086v3.762h6.24v2.07h-6.24v9.75c0 3.045.814 4.71 3.27 4.71 1.87 0 3.484-.99 4.755-2.512l.814.56c-1.528 2.425-3.927 3.76-7.182 3.76-3.812 0-6.554-1.853-6.554-5.9V21.104h.027zm25.633-8.085l-4.598 2.282c1.514.905 1.8 2.585 1.8 6.09v9.133c0 3.474 1.47 6.088 4.968 6.088 4.356 0 5.827-3.044 5.827-6.045v-9.19c0-3.475-.514-5.14-1.985-6.088l4.827-2.283h1.042v18.135l1.899 3.574v.517h-5.64v-2.383c-1.041 1.58-2.513 3.044-6.297 3.044-3.498 0-8.468-1.622-8.468-8.04V19.31c0-3.474-.286-5.183-1.8-6.087l4.598-2.283h1.085v1.079H99.52zm22.263 9.19c1.513-5.845 5.44-9.19 9.653-9.19 2.028 0 3.713.618 4.698 1.78v6.532h-1.086c-.814-4.68-3.313-7.078-6.126-7.078-4.87 0-7.14 4.737-7.14 9.85v5.1c0 3.475 1.47 6.09 4.97 6.09h.428l2.456-1.005v1.004h-12.91v-.43l2.456-3.618v-12.75c0-3.474-.286-5.183-1.8-6.087l4.598-2.283h1.043v11.085h-.24zm23.048 11.802l-2.456 3.619v.43h8.71v-.43l-2.37-3.662V9.62c0-3.518-.857-5.14-2.37-6.145l-2.657-2.814h1.042v30.898l-.014.001zm4.213-35.218c0 1.623-1.285 2.928-2.899 2.928-1.613 0-2.899-1.305-2.899-2.928 0-1.622 1.286-2.928 2.9-2.928 1.613 0 2.898 1.306 2.898 2.928m6.168 35.218l2.456-3.619V9.62c0-3.518-.857-5.14-2.37-6.145l-2.657-2.814h1.043v14.905c1.556-1.966 4.255-4.034 8.24-4.034 3.499 0 8.468 1.622 8.468 8.04v12.852l2.456 3.619v.43h-8.71v-.43l2.37-3.662V19.74c0-3.475-1.47-6.09-4.969-6.09-4.355 0-5.826 3.044-5.826 6.046v12.29l2.37 3.662v.43h-8.711v-.43zm30.702-18.62c4.484 0 7.854 2.97 7.854 8.41v.862h-14.993c0 4.98 2.513 9.763 7.668 9.763 2.97 0 5.184-1.363 6.712-3.86l.9.403c-1.086 2.785-3.927 5.328-7.982 5.328-6.126 0-10.71-4.423-10.71-11.186 0-6.763 4.37-10.72 10.551-10.72zm-7.14 7.899h10.395c-.1-5.026-2.799-6.664-5.441-6.664-3.613 0-5.741 3.432-4.955 6.664zm16.536 10.72l2.456-3.619V9.62c0-3.518-.857-5.14-2.37-6.145l-2.657-2.814h1.043v30.897l2.37 3.663v.43h-8.71v-.43zm-152.264 24.79c0 5.714-3.999 9.287-10.253 9.287-2.799 0-5.155-.99-6.64-2.756v2.095h-5.84v-.373l2.342-3.461V40.73l-2.456-3.733v-.373h9.853c7.24 0 10.367 2.126 10.367 6.72 0 3.36-2.67 5.987-6.94 6.837 5.897 0 9.567 3.39 9.567 8.27zm-16.622-13.353V43.86h2.856c4.298 0 7.312-2.24 7.312-6.548 0-3.762-2.228-5.555-6.912-5.555h-3.256v.015zm12.81 21.078c0-4.912-2.998-7.725-8.167-7.725h-4.656v11.242c1.142 2.083 3.37 3.259 6.14 3.259 4.427 0 6.712-2.656 6.712-6.78m4.741-13.166c0-4.897 4.284-7.884 9.31-7.884 5.027 0 9.325 3.36 9.325 9.922 0 5.988-4.512 9.62-9.253 9.62-5.356 0-9.382-3.404-9.382-9.65zm15.893.345c0-5.47-2.627-9.265-6.454-9.265-3.613 0-5.897 3.23-5.897 8.294 0 5.63 2.756 9.52 6.826 9.52 3.37 0 5.525-3.316 5.525-8.55m6.183 8.624l2.114-3.102V45.28c0-3.015-.243-4.45-1.542-5.226l3.955-1.966h.9v2.555c1.557-1.781 3.642-2.899 6.498-2.899 2.998 0 7.24 1.392 7.24 6.893v11.013l2.113 3.101v.374h-7.468v-.374l2.028-3.143V45.38c0-2.987-1.257-5.226-4.255-5.226-3.727 0-5.013 2.612-5.013 5.197v10.783l2.028 3.143v.374h-7.469v-.374h-.129zm22.72 0 2.113-3.102V45.28c0-3.015-.243-4.45-1.542-5.226l3.956-1.966h.9v2.555c1.556-1.781 3.641-2.899 6.497-2.899 2.998 0 7.24 1.392 7.24 6.893v11.013l2.114 3.101v.374h-7.469v-.374l2.028-3.143V45.38c0-2.987-1.256-5.226-4.255-5.226-3.727 0-5.012 2.612-5.012 5.197v10.783l2.028 3.143v.374h-7.469v-.374h-.129zm21.12 0 2.113-3.102V35.735c0-3.015-.728-4.408-2.028-5.268l-2.27-2.411h.9v26.507l2.028 3.143v.374h-7.468v-.374zm3.613-30.183c0 1.392-1.1 2.512-2.484 2.512a2.508 2.508 0 0 1-2.485-2.512c0-1.392 1.1-2.512 2.485-2.512 1.384 0 2.484 1.12 2.484 2.512m5.17 30.183 2.114-3.102V35.735c0-3.015-.728-4.408-2.029-5.268l-2.27-2.411h.9v12.75c1.328-1.695 3.642-3.46 7.055-3.46 2.999 0 7.24 1.392 7.24 6.893v11.013l2.114 3.101v.374h-7.469v-.374l2.028-3.143V45.38c0-2.987-1.256-5.226-4.255-5.226-3.727 0-5.012 2.612-5.012 5.197v10.783l2.028 3.143v.374h-7.469v-.374zm26.29-15.951c3.827 0 6.712 2.54 6.712 7.208v.734h-12.824c0 4.25 2.157 8.35 6.555 8.35 2.542 0 4.427-1.162 5.74-3.303l.771.344c-.928 2.382-3.357 4.553-6.826 4.553-5.241 0-9.153-3.79-9.153-9.578 0-5.787 3.741-9.308 9.025-9.308zm-6.112 6.763h8.896c-.086-4.308-2.399-5.714-4.655-5.714-3.085 0-4.926 2.94-4.241 5.714z" fill="#69013B"/></svg>'''

OSP_BLOCKS = [
    {
        "id": "osp1",
        "title": "Teoria",
        "subtitle": "Tekoälyn teoria ja toimintaperiaatteet",
        "color": "#69013B",
        "icon": "📐",
        "lessons": [
            ("lesson-01", "Älykäs vai sääntö? — mitä tekoäly oikeasti tekee", "teaching"),
            ("lesson-02", "Viisi tekoälyn tasoa — missä mennään ja mihin ollaan menossa", "teaching"),
            ("lesson-03", "Miten kone kirjoittaa? — generatiivisen AI:n mekaniikka", "teaching"),
            ("lesson-04", "Konteksti ratkaisee — miksi sama kysymys antaa eri vastauksen", "teaching"),
            ("lesson-05", "Muistin rajat — kuinka paljon tekoäly oikeasti muistaa", "teaching"),
            ("lesson-06", "Kuvat, ääni ja teksti — kun sanat eivät riitä", "teaching"),
            ("lesson-07", "Miksi tekoäly valehtelee? — hallusinaatiot ja satunnaisuus", "teaching"),
            ("lesson-08", "Kenen teksti se on? — etiikka, oikeudet ja vastuu", "teaching"),
            ("lesson-09", "Tuomaripöydän päätös — asiantuntijalausunto tekoälystä", "teaching"),
        ]
    },
    {
        "id": "osp2",
        "title": "Tekoälyjen käyttö",
        "subtitle": "Generatiivisten tekoälytyökalujen käyttö",
        "color": "#1D4ED8",
        "icon": "🛠",
        "lessons": [
            ("lesson-10", "Kilpailuta tekoälyt — mikä työkalu mihinkin?", "teaching"),
            ("lesson-11", "Muita tekoälymalleja — kuin ChatGPT ja Claude", "teaching"),
            ("lesson-12", "Anna konteksti — miten saat parempia vastauksia", "teaching"),
            ("lesson-13", "AI työparina — käytännön hyöty arjessa ja opiskelussa", "teaching"),
            ("lesson-14", "Oma botti I — suunnittelu, ohjeet ja persoona", "teaching"),
            ("lesson-15", "Oma botti II — tietopohja, rajaukset ja testaus", "teaching"),
            ("lesson-16", "Tekoälytyökalut erikoisaloilla — kuva, musiikki, video ja koodi", "teaching"),
            ("lesson-17", "Projektidokumenttibotti — suunnittele ja aloita rakentaminen", "teaching"),
            ("lesson-18", "Projektidokumenttibotti — viimeistele ja esittele", "assessment"),
        ]
    },
    {
        "id": "osp3",
        "title": "Agentit",
        "subtitle": "Tekoälyagentit ja automaatio",
        "color": "#065F46",
        "icon": "🤖",
        "lessons": [
            ("lesson-19", "Boteista agentteihin — mikä muuttuu kun AI toimii itsenäisesti", "teaching"),
            ("lesson-20", "Automaatio vai autonomia? — milloin agentti kannattaa", "teaching"),
            ("lesson-21", "Agentin muisti ja konteksti — miten kone pysyy kartalla", "teaching"),
            ("lesson-22", "Agentin työkalut — tiedostot, haku ja komennot", "teaching"),
            ("lesson-23", "Suunnittelumallit — ReAct, ketjuajattelu ja orkestrointi", "teaching"),
            ("lesson-24", "Turvallisuus ensin — hyökkäykset, suojaukset ja lokitus", "teaching"),
            ("lesson-25", "Ihminen portinvartijana — human-in-the-loop käytännössä", "teaching"),
            ("lesson-26", "Kädet saveen — n8n-agenttipaja alkaa", "teaching"),
            ("lesson-27", "Viimeistele ja esittele — agenttisi on valmis", "assessment"),
        ]
    }
]

# Google Slides embed URLs per lesson (None = no slides for this lesson)
SLIDE_URLS = {
    "intro":     "https://docs.google.com/presentation/d/1wFcG2PM71QAN3IgFCxdMj8zZAK2Q2iGpEkW1O_sn4W0/embed?start=false&loop=false&delayms=3000",
    "lesson-01": "https://docs.google.com/presentation/d/1bWogMlO8ip24mjXfZ6vDAqXngFsAOcLy5dJ0bwZR_mA/embed?start=false&loop=false&delayms=3000",
    "lesson-02": "https://docs.google.com/presentation/d/14QH5M5HHObUlFZ_kFbmcNiNWn916HlyW10Q0kQmkTMk/embed?start=false&loop=false&delayms=3000",
    "lesson-03": "https://docs.google.com/presentation/d/18JiTuqSbkvTHbjkgmak1t4Yi6FFpws4OiQY7OlUx-VQ/embed?start=false&loop=false&delayms=3000",
    "lesson-04": "https://docs.google.com/presentation/d/1AYtG5_qN8i-peKPteaKjViK12pL9pbhVVXTRABou_P8/embed?start=false&loop=false&delayms=3000",
    "lesson-05": "https://docs.google.com/presentation/d/1hWZhtcmZrzBsIz5OxD7Khjz73GDI0wIzs78neRQTT0w/embed?start=false&loop=false&delayms=3000",
    "lesson-06": "https://docs.google.com/presentation/d/1X8X3CC9JTTkdcfZPtxuHhHCF19F6Ye3QusvphjPhzog/embed?start=false&loop=false&delayms=3000",
    "lesson-07": "https://docs.google.com/presentation/d/1NqzZSCOLQiz9eo_lZKa-_VjEmeU3MFFNgVWTiHQ_x-8/embed?start=false&loop=false&delayms=3000",
    "lesson-08": "https://docs.google.com/presentation/d/1Juoruyp1kibxlQyMreH_jDljSjFtasiTF2DvISpTZG4/embed?start=false&loop=false&delayms=3000",
    "lesson-09": "https://docs.google.com/presentation/d/1HEHaQTA_iUfOVaRwiGe_nbjDlJTi8AqE8NPJeLhOJPE/embed?start=false&loop=false&delayms=3000",
    "lesson-10": "https://docs.google.com/presentation/d/1O3_d4Mxtw9lFCxFbvg1MGq764388HcZK9HZuB-t_9VM/embed?start=false&loop=false&delayms=3000",
    "lesson-11": "https://docs.google.com/presentation/d/1F_flMJrYp_3NNtc30GfZyPyc06y9sURS_rQWpOKUIRA/embed?start=false&loop=false&delayms=3000",
    "lesson-12": None,  # Anna konteksti — puuttuu
    "lesson-13": "https://docs.google.com/presentation/d/1vnW47D7Sf50Kkrfr8S5ZWERv04krZ1RrSfdR2LPT7zk/embed?start=false&loop=false&delayms=3000",
    "lesson-14": "https://docs.google.com/presentation/d/1ftouC0GjjHegb3v0hHGFCJP8jEKGgDnAN5s2FFYML4I/embed?start=false&loop=false&delayms=3000",
    "lesson-15": "https://docs.google.com/presentation/d/1Hoif5gNFdzchpWgD1XRe_Dqa3lH5ANt8vnng0qifOYE/embed?start=false&loop=false&delayms=3000",
    "lesson-16": "https://docs.google.com/presentation/d/1MoRLKjy-Jje8wH6OPiasB3Rea0MIUNwNoGyup7N45bk/embed?start=false&loop=false&delayms=3000",
    "lesson-17": "https://docs.google.com/presentation/d/1Fg4VffcQVKhjoqd8FPKTfFVoQ7GZPa2Ro71lKJzwNk0/embed?start=false&loop=false&delayms=3000",
    "lesson-18": "https://docs.google.com/presentation/d/1g2kf-efRceTe4Ddfi0K5GP1Dgfr6f-WRFYbmJ4or1SQ/embed?start=false&loop=false&delayms=3000",
    "lesson-19": "https://docs.google.com/presentation/d/1Hd-UPJb4Kq1jTob8ZELAWOvyqVI73VzhbHn1vJtK3kc/embed?start=false&loop=false&delayms=3000",
    "lesson-20": "https://docs.google.com/presentation/d/1Z6R08URnRqV90ZilaxAOKZQmNjJzt83VV3SFUAyeGY0/embed?start=false&loop=false&delayms=3000",
    "lesson-21": "https://docs.google.com/presentation/d/1qESN1GJVfxoxmctns0hZtLjBbQppfC8NVWYpaMMFqUY/embed?start=false&loop=false&delayms=3000",
    "lesson-22": "https://docs.google.com/presentation/d/1uDG8qf8Vt6HV9a3v_sbtSzHOkappvvjzPywGNvYPA3Q/embed?start=false&loop=false&delayms=3000",
    "lesson-23": "https://docs.google.com/presentation/d/1uUElHRQ2s49QQRCyMl-Ut5nYOAGizhc4mfIW0feH2Qc/embed?start=false&loop=false&delayms=3000",
    "lesson-24": "https://docs.google.com/presentation/d/1m_NFiAz1ugEQ9tnYzADcJkE1SaubUJNKdGlfW5dz_TQ/embed?start=false&loop=false&delayms=3000",
    "lesson-25": "https://docs.google.com/presentation/d/1pIAbc7ljDWq7qRpsF3CMzVMqB5p3PbM_uH4IBkLCums/embed?start=false&loop=false&delayms=3000",
    "lesson-26": "https://docs.google.com/presentation/d/1AGsW7y5WyiGH5-5fgEchsya36cjLgIA7xmGBpyNdtI8/embed?start=false&loop=false&delayms=3000",
    "lesson-27": "https://docs.google.com/presentation/d/10g_dfNrEnFhVnV4ymbeGlAXv3oshjx-A8NoPja0bQW0/embed?start=false&loop=false&delayms=3000",
}

# Standalone review slides (shown on home page)
REVIEW_SLIDE_URL = "https://docs.google.com/presentation/d/1o2nKDyvDjkIYQtd3QUgB_z-X78iA92TQVxO7Lyk6Dqk/embed?start=false&loop=false&delayms=3000"

MD_EXTENSIONS = ['tables', 'fenced_code', 'nl2br']


def read_file(path):
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            return f.read()
    return ''


def to_html(text):
    if not text:
        return '<p><em>(Tiedostoa ei löydy)</em></p>'
    # Convert mermaid fenced blocks to placeholder divs BEFORE markdown processing
    # This prevents fenced_code from turning them into <code> blocks
    mermaid_blocks = []
    def _stash_mermaid(m):
        idx = len(mermaid_blocks)
        mermaid_blocks.append(m.group(1).strip())
        return f'MERMAID_PLACEHOLDER_{idx}'
    text = re.sub(r'```mermaid\s*\n(.*?)```', _stash_mermaid, text, flags=re.DOTALL)

    text = re.sub(r'\*\*Pysähdy hetkeksi:(.*?)\*\*',
                  r'> **Pysähdy hetkeksi:\1**', text, flags=re.DOTALL)
    text = re.sub(r'^Pysähdy hetkeksi:(.*?)$',
                  r'> **Pysähdy hetkeksi:**\1', text, flags=re.MULTILINE)
    h = md_lib.markdown(text, extensions=MD_EXTENSIONS)
    h = re.sub(r'<blockquote>\s*<p>', '<blockquote class="pause"><p>', h)
    h = re.sub(r'<p><strong>Jos teet tehtävän yksin',
               '<p class="solo-note"><strong>Jos teet tehtävän yksin', h)
    h = re.sub(r'<h2>(Tehtävä \d+[\.\-]\d+.*?)</h2>',
               r'<h2 class="task-header">\1</h2>', h)

    # Restore mermaid blocks as <div class="mermaid"> elements
    for i, block in enumerate(mermaid_blocks):
        h = h.replace(f'MERMAID_PLACEHOLDER_{i}',
                       f'<div class="mermaid">\n{block}\n</div>')
        h = h.replace(f'<p>MERMAID_PLACEHOLDER_{i}</p>',
                       f'<div class="mermaid">\n{block}\n</div>')

    return h


def to_html_with_cards(text, include_h3=False):
    """Convert markdown to HTML and wrap task/section blocks in styled cards.
    Use ONLY for student-tasks, teacher-led-tasks, and teacher-materials panels.
    include_h3=True: also wrap h3-level sections as sub-cards (for teacher materials).
    include_h3=False: only wrap h2-level sections (for student/teacher-led tasks)."""
    h = to_html(text)
    return _wrap_task_cards(h, include_h3=include_h3)


def _classify_heading(title: str) -> str:
    """Determine card type from heading text."""
    title_lower = title.lower()
    if any(w in title_lower for w in ['väärinkäsitys', 'osaamistavoite', 'osaamistavoitteet',
                                       'cfu-kysym', 'cfu kysym', 'yleisi', 'yleiset']):
        return 'info'
    if any(w in title_lower for w in ['pisteet', 'arviointi', 'odotettu tuotos']):
        return 'assessment'
    if any(w in title_lower for w in ['lisäresurss', 'lisämateriaali', 'resurss']):
        return 'resource'
    return 'task'


def _wrap_task_cards(html: str, include_h3: bool = False) -> str:
    """Wrap each task/section block in a styled card div.

    include_h3=False: only h2 headings become cards (h3 stays inside the card body).
    include_h3=True:  both h2 and h3 headings become cards (for teacher materials).
    """

    htags = 'h[23]' if include_h3 else 'h2'
    heading_re = re.compile(
        rf'<({htags})[^>]*>(.*?)</\1>'
    )

    # Headings that should NOT become cards (too generic or are the page title)
    _SKIP_HEADINGS = {'Tehtävät', 'Opiskelutehtävät', 'Sanasto'}

    parts = []
    last_end = 0
    in_card = False

    for m in heading_re.finditer(html):
        tag = m.group(1)   # h2 or h3
        title = m.group(2)
        # Strip any inner HTML tags for classification
        title_text = re.sub(r'<[^>]+>', '', title).strip()

        # Skip page-level h1 (not matched anyway) and generic wrapper headings
        if title_text in _SKIP_HEADINGS:
            continue

        # Skip very short headings that are just labels (e.g. "Ohjeet")
        # But keep anything that looks like a real section
        if len(title_text) < 4:
            continue

        ct = _classify_heading(title_text)

        # For h3 inside an already-open h2 card: close the h2 card first
        # For h2 or h3: close previous card if open
        if in_card:
            content_before = html[last_end:m.start()]
            content_before = re.sub(r'\s*<hr\s*/?\s*>\s*$', '', content_before)
            parts.append(content_before)
            parts.append('</div></div>')  # close .task-card-body + .task-card

        else:
            content_before = html[last_end:m.start()]
            content_before = re.sub(r'\s*<hr\s*/?\s*>\s*$', '', content_before)
            parts.append(content_before)

        # h3 cards are slightly smaller (nested style)
        size_cls = ' task-card--sm' if tag == 'h3' else ''

        parts.append(f'<div class="task-card task-card--{ct}{size_cls}">')
        parts.append(f'<div class="task-card-header"><{tag}>{title}</{tag}></div>')
        parts.append('<div class="task-card-body">')

        in_card = True
        last_end = m.end()

    # Remaining content
    if in_card:
        remaining = html[last_end:]
        remaining = re.sub(r'\s*<hr\s*/?\s*>\s*$', '', remaining)
        parts.append(remaining)
        parts.append('</div></div>')
    else:
        parts.append(html[last_end:])

    return ''.join(parts)


def build_lesson_data():
    data = {}
    for osp in OSP_BLOCKS:
        for lid, short_title, btype in osp['lessons']:
            sdir = f"{BASE}/student/{lid}"
            tdir = f"{BASE}/teacher/{lid}"
            slide_url = SLIDE_URLS.get(lid)
            slides_html = ''
            if slide_url:
                slides_html = (
                    f'<div class="slides-container">'
                    f'<iframe src="{slide_url}" frameborder="0" '
                    f'width="100%" height="569" allowfullscreen="true" '
                    f'mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>'
                    f'</div>'
                )
            data[lid] = {
                'osp_id':        osp['id'],
                'osp_title':     osp['title'],
                'osp_color':     osp['color'],
                'osp_icon':      osp['icon'],
                'short_title':   short_title,
                'block_type':    btype,
                'slides':        slides_html,
                'selfstudy':     to_html(read_file(f"{sdir}/self-study.md")),
                'vocab':         to_html(read_file(f"{sdir}/vocabulary.md")),
                'stasks':        to_html_with_cards(read_file(f"{sdir}/student-tasks.md"), include_h3=False),
                'tltasks':       to_html_with_cards(read_file(f"{tdir}/teacher-led-tasks.md"), include_h3=False),
                'tmats':         to_html_with_cards(read_file(f"{tdir}/teacher-materials.md"), include_h3=True),
            }
    return data


def esc_js(s):
    return s.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')


def generate_html(data):
    all_ids = [lid for osp in OSP_BLOCKS for lid, _, _ in osp['lessons']]

    # Build OSP accordion cards for home page
    osp_cards_html = ''
    for osp in OSP_BLOCKS:
        lessons_in_osp = osp['lessons']
        lessons_html = ''
        for idx, (lid, short_title, btype) in enumerate(lessons_in_osp, 1):
            global_idx = all_ids.index(lid) + 1
            icon = '★' if btype == 'assessment' else '📖'
            lessons_html += f'''      <button class="acc-lesson" onclick="loadLesson('{lid}')">
        <span class="acc-l-num">{global_idx}</span>
        <span class="acc-l-title">{short_title}</span>
        <span class="acc-l-icon">{icon}</span>
        <span class="acc-l-check" id="done-{lid}"></span>
      </button>'''

        osp_cards_html += f'''  <div class="osp-card" style="--osp-color:{osp['color']}">
    <div class="osp-card-head" onclick="toggleAcc(this)">
      <div class="osp-icon">{osp['icon']}</div>
      <div class="osp-card-info">
        <div class="osp-title">{osp['title']}</div>
        <div class="osp-subtitle">{osp['subtitle']}</div>
      </div>
      <div class="osp-meta">
        <div class="osp-count">{len(lessons_in_osp)} oppituntia</div>
        <div class="acc-chevron">▼</div>
      </div>
    </div>
    <div class="osp-card-lessons">
{lessons_html}
    </div>
    <div class="osp-card-progress">
      <div class="prog-bar"><div class="prog-fill" id="pfill-{osp['id']}" style="background:{osp['color']}"></div></div>
      <span class="prog-text" id="ptxt-{osp['id']}">0 / {len(lessons_in_osp)}</span>
    </div>
  </div>
'''

    # JS lesson data
    js_items = []
    for lid, d in data.items():
        js_items.append(
            f'  "{lid}": {{\n'
            f'    ospId:"{d["osp_id"]}",ospTitle:`{esc_js(d["osp_title"])}`,\n'
            f'    ospColor:"{d["osp_color"]}",ospIcon:"{d["osp_icon"]}",\n'
            f'    shortTitle:`{esc_js(d["short_title"])}`,blockType:"{d["block_type"]}",\n'
            f'    slides:`{esc_js(d["slides"])}`,\n'
            f'    selfstudy:`{esc_js(d["selfstudy"])}`,\n'
            f'    vocab:`{esc_js(d["vocab"])}`,\n'
            f'    stasks:`{esc_js(d["stasks"])}`,\n'
            f'    tltasks:`{esc_js(d["tltasks"])}`,\n'
            f'    tmats:`{esc_js(d["tmats"])}`,\n'
            f'  }}'
        )
    js_data = 'const L={' + ',\n'.join(js_items) + '};'

    osp_meta_js = json.dumps([
        {"id": o["id"], "ids": [lid for lid, _, _ in o["lessons"]]}
        for o in OSP_BLOCKS
    ])

    # Complete HTML
    return f'''<!DOCTYPE html>
<html lang="fi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Tekoälyn perusteet — Business College Helsinki</title>
<style>
:root{{
  --bc-primary:#69013B;--bc-dark:#4D0128;
  --bg-paper:#FAF9F6;--bg-white:#FFFFFF;
  --border-soft:#E8E0D8;--border-light:#F0DDD1;
  --text-dark:#1F2937;--text-muted:#6B7280;--text-light:#9CA3AF;
  --r:12px;--r-sm:8px;
}}
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap');
html{{font-size:16px}}
body{{
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",sans-serif;
  background:var(--bg-paper);
  color:var(--text-dark);
  line-height:1.6;
}}

/* ============ TOP NAVIGATION ============ */
.topbar{{
  background:var(--bg-white);
  border-bottom:1px solid var(--border-soft);
  display:flex;
  align-items:center;
  justify-content:space-between;
  padding:16px 32px;
  gap:20px;
  position:sticky;
  top:0;
  z-index:100;
}}
.logo-group{{
  display:flex;
  align-items:center;
  gap:16px;
}}
.logo-text{{
  display:flex;
  flex-direction:column;
  line-height:1.1;
  cursor:pointer;
}}
.logo-text .logo-main{{
  font-family:'Playfair Display',Georgia,'Times New Roman',serif;
  font-size:22px;
  font-weight:400;
  color:var(--bc-primary);
  letter-spacing:0.01em;
}}
.logo-text .logo-sub{{
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  font-size:9px;
  font-weight:600;
  color:var(--bc-primary);
  letter-spacing:0.25em;
  text-transform:uppercase;
  margin-top:1px;
}}
.topbar-title{{
  font-size:13px;
  font-weight:700;
  color:var(--bc-primary);
  letter-spacing:0.05em;
  text-transform:uppercase;
}}
.topbar-right{{
  display:flex;
  align-items:center;
  gap:20px;
  margin-left:auto;
}}
.progress-bar{{
  width:120px;
  height:5px;
  background:var(--border-light);
  border-radius:3px;
  overflow:hidden;
}}
.progress-fill{{
  height:100%;
  background:var(--bc-primary);
  width:0;
  transition:width 0.4s ease;
  border-radius:3px;
}}
.progress-text{{
  font-size:11px;
  font-weight:600;
  color:var(--text-muted);
  white-space:nowrap;
}}

/* ============ MAIN LAYOUT ============ */
.container{{
  max-width:820px;
  margin:0 auto;
  padding:60px 32px;
}}

/* ============ HERO (HOME) ============ */
.hero{{
  margin-bottom:80px;
  text-align:center;
}}
.hero-eyebrow{{
  font-size:11px;
  font-weight:700;
  color:var(--bc-primary);
  text-transform:uppercase;
  letter-spacing:0.08em;
  margin-bottom:12px;
}}
.hero-title{{
  font-size:48px;
  font-weight:900;
  color:var(--text-dark);
  line-height:1.1;
  letter-spacing:-0.02em;
  margin-bottom:12px;
}}
.hero-subtitle{{
  font-size:18px;
  color:var(--text-muted);
  margin-bottom:32px;
  line-height:1.5;
}}
.hero-stats{{
  display:flex;
  justify-content:center;
  gap:20px;
  flex-wrap:wrap;
}}
.stat-chip{{
  background:var(--bg-white);
  border:1px solid var(--border-soft);
  border-radius:var(--r-sm);
  padding:14px 20px;
  text-align:center;
  min-width:100px;
}}
.stat-value{{
  font-size:28px;
  font-weight:900;
  color:var(--bc-primary);
  line-height:1;
}}
.stat-label{{
  font-size:10px;
  color:var(--text-muted);
  margin-top:4px;
  font-weight:600;
}}

/* ============ OSP CARDS (ACCORDION) ============ */
.osp-cards{{
  margin:60px 0;
}}
.osp-card{{
  background:var(--bg-white);
  border:1px solid var(--border-soft);
  border-left:5px solid var(--osp-color);
  border-radius:var(--r);
  margin-bottom:20px;
  overflow:hidden;
  box-shadow:0 1px 3px rgba(0,0,0,0.04);
  transition:all 0.2s ease;
}}
.osp-card:hover{{
  box-shadow:0 4px 12px rgba(0,0,0,0.08);
  border-color:var(--border-soft);
}}
.osp-card-head{{
  padding:24px;
  display:flex;
  align-items:center;
  gap:18px;
  cursor:pointer;
  user-select:none;
  transition:background 0.15s;
}}
.osp-card-head:hover{{
  background:rgba(105, 1, 59, 0.02);
}}
.osp-icon{{
  font-size:28px;
  flex-shrink:0;
}}
.osp-card-info{{
  flex:1;
  text-align:left;
}}
.osp-title{{
  font-size:16px;
  font-weight:700;
  color:var(--text-dark);
  margin-bottom:4px;
}}
.osp-subtitle{{
  font-size:13px;
  color:var(--text-muted);
  line-height:1.4;
}}
.osp-meta{{
  display:flex;
  flex-direction:column;
  align-items:flex-end;
  gap:8px;
  flex-shrink:0;
}}
.osp-count{{
  font-size:12px;
  color:var(--text-light);
  font-weight:600;
}}
.acc-chevron{{
  font-size:12px;
  color:var(--text-muted);
  transition:transform 0.3s ease;
}}
.osp-card-head[onclick].open .acc-chevron{{
  transform:rotate(180deg);
}}
.osp-card-lessons{{
  border-top:1px solid var(--border-light);
  display:flex;
  flex-direction:column;
  max-height:0;
  overflow:hidden;
  transition:max-height 0.4s cubic-bezier(0,0,0.2,1);
}}
.osp-card-lessons.open{{
  max-height:2000px;
}}
.acc-lesson{{
  display:flex;
  align-items:center;
  gap:12px;
  padding:14px 24px;
  border:none;
  background:none;
  text-align:left;
  cursor:pointer;
  border-bottom:1px solid var(--border-light);
  font-size:14px;
  color:var(--text-dark);
  transition:background 0.1s;
}}
.acc-lesson:last-child{{
  border-bottom:none;
}}
.acc-lesson:hover{{
  background:rgba(105, 1, 59, 0.03);
}}
.acc-lesson.done{{
  color:var(--text-light);
}}
.acc-l-num{{
  display:flex;
  align-items:center;
  justify-content:center;
  min-width:32px;
  height:32px;
  background:var(--osp-color,var(--bc-primary));
  color:var(--bg-white);
  border-radius:50%;
  font-size:12px;
  font-weight:700;
  flex-shrink:0;
}}
.acc-l-title{{
  flex:1;
  font-weight:500;
}}
.acc-lesson.done .acc-l-title{{
  text-decoration:line-through;
}}
.acc-l-icon{{
  font-size:13px;
  color:var(--text-muted);
  flex-shrink:0;
}}
.acc-l-check{{
  width:20px;
  height:20px;
  border:2px solid var(--border-soft);
  border-radius:3px;
  flex-shrink:0;
  transition:all 0.2s;
  display:flex;
  align-items:center;
  justify-content:center;
  font-size:12px;
  font-weight:700;
  color:var(--bg-white);
}}
.acc-lesson.done .acc-l-check{{
  background:#059669;
  border-color:#059669;
}}
.acc-lesson.done .acc-l-check::after{{
  content:'✓';
}}
.osp-card-progress{{
  padding:16px 24px;
  border-top:1px solid var(--border-light);
  display:flex;
  align-items:center;
  gap:12px;
}}
.prog-bar{{
  flex:1;
  height:6px;
  background:var(--border-light);
  border-radius:3px;
  overflow:hidden;
}}
.prog-fill{{
  height:100%;
  width:0;
  transition:width 0.5s ease;
}}
.prog-text{{
  font-size:11px;
  color:var(--text-muted);
  font-weight:600;
  min-width:60px;
  text-align:right;
}}

/* ============ INFO BOX ============ */
.info-box{{
  background:var(--bg-white);
  border:1px solid var(--border-soft);
  border-radius:var(--r);
  padding:24px 28px;
  margin:60px 0;
  font-size:14px;
  line-height:1.8;
  color:var(--text-muted);
}}
.info-box strong{{
  color:var(--text-dark);
  font-weight:600;
}}
.info-box br{{
  content:"";
  display:block;
  margin:8px 0;
}}

/* ============ LESSON VIEW ============ */
.lesson-view{{
  display:none;
}}
.lesson-view.active{{
  display:flex;
  flex-direction:column;
  min-height:100vh;
}}
.lesson-header{{
  background:var(--bg-white);
  border-bottom:1px solid var(--border-soft);
  padding:40px 32px;
  margin-bottom:0;
}}
.breadcrumb{{
  font-size:12px;
  color:var(--text-muted);
  margin-bottom:12px;
  display:flex;
  align-items:center;
  gap:8px;
}}
.bc-link{{
  color:var(--bc-primary);
  cursor:pointer;
  font-weight:600;
}}
.bc-link:hover{{
  text-decoration:underline;
}}
.lesson-title{{
  font-size:36px;
  font-weight:900;
  color:var(--text-dark);
  line-height:1.2;
  letter-spacing:-0.02em;
  margin-bottom:16px;
}}
.lesson-badges{{
  display:flex;
  gap:10px;
  flex-wrap:wrap;
}}
.badge{{
  display:inline-flex;
  align-items:center;
  gap:4px;
  font-size:11px;
  font-weight:700;
  padding:6px 12px;
  border-radius:20px;
  text-transform:uppercase;
  letter-spacing:0.05em;
}}
.badge-osp{{
  background:rgba(105,1,59,0.1);
  color:var(--bc-primary);
}}
.badge-type{{
  background:#EFF6FF;
  color:#1D4ED8;
}}
.badge-assess{{
  background:#FEF3C7;
  color:#92400E;
}}

/* ============ TABS ============ */
.lesson-tabs{{
  display:flex;
  border-bottom:2px solid var(--border-soft);
  background:var(--bg-white);
  padding:0 32px;
  overflow-x:auto;
  gap:0;
}}
.tab-btn{{
  padding:14px 18px;
  border:none;
  background:none;
  cursor:pointer;
  font-size:14px;
  font-weight:600;
  color:var(--text-muted);
  border-bottom:3px solid transparent;
  margin-bottom:-2px;
  transition:all 0.2s;
  white-space:nowrap;
}}
.tab-btn:hover{{
  color:var(--bc-primary);
}}
.tab-btn.active{{
  color:var(--bc-primary);
  border-bottom-color:var(--bc-primary);
}}

/* ============ LESSON CONTENT ============ */
.lesson-panels{{
  flex:1;
  padding:40px 32px;
  overflow-y:auto;
}}
.panel{{
  display:none;
  max-width:780px;
  margin:0 auto;
}}
.panel.active{{
  display:block;
}}
.slides-container{{
  position:relative;
  width:100%;
  padding-top:8px;
}}
.slides-container iframe{{
  width:100%;
  height:min(569px,56vw);
  border:1px solid var(--border-soft);
  border-radius:var(--r-sm);
}}
.panel h1{{
  font-size:24px;
  font-weight:800;
  margin:28px 0 12px;
  color:var(--text-dark);
  letter-spacing:-0.01em;
}}
.panel h1:first-child{{
  margin-top:0;
}}
.panel h2{{
  font-size:18px;
  font-weight:700;
  margin:24px 0 10px;
  color:var(--text-dark);
}}
.panel h3{{
  font-size:15px;
  font-weight:700;
  margin:16px 0 8px;
  color:var(--text-dark);
}}
.panel p{{
  margin:0 0 14px;
  color:var(--text-muted);
  line-height:1.75;
}}
.panel strong{{
  color:var(--text-dark);
  font-weight:700;
}}
.panel em{{
  font-style:italic;
}}
.panel a{{
  color:var(--bc-primary);
  text-decoration:none;
  font-weight:600;
}}
.panel a:hover{{
  text-decoration:underline;
}}
.panel ul,.panel ol{{
  margin:10px 0 14px 22px;
}}
.panel li{{
  margin-bottom:6px;
  color:var(--text-muted);
  line-height:1.7;
}}
.panel code{{
  background:#F3F4F6;
  padding:3px 8px;
  border-radius:4px;
  font-family:"Fira Code","SF Mono",Consolas,monospace;
  font-size:13px;
  color:var(--bc-dark);
}}
.panel pre{{
  background:#1E293B;
  color:#E2E8F0;
  padding:16px 20px;
  border-radius:var(--r-sm);
  overflow-x:auto;
  margin:16px 0 18px;
  font-family:"Fira Code","SF Mono",Consolas,monospace;
  font-size:13px;
  line-height:1.6;
}}
.panel pre code{{
  background:none;
  padding:0;
  color:inherit;
  font-size:inherit;
  font-family:inherit;
}}
.panel table{{
  border-collapse:collapse;
  width:100%;
  margin:14px 0 18px;
  font-size:14px;
}}
.panel th{{
  background:#F8FAFC;
  padding:10px 14px;
  text-align:left;
  border:1px solid var(--border-soft);
  font-weight:700;
  font-size:12px;
  color:var(--text-dark);
}}
.panel td{{
  padding:10px 14px;
  border:1px solid var(--border-soft);
  color:var(--text-muted);
}}
.panel hr{{
  border:none;
  border-top:1px solid var(--border-light);
  margin:24px 0;
}}
.panel blockquote{{
  border-left:4px solid var(--border-light);
  padding:14px 18px;
  background:#F9FAFB;
  border-radius:0 var(--r-sm) var(--r-sm) 0;
  margin:16px 0;
  color:var(--text-muted);
}}
.panel blockquote.pause{{
  background:#FEF9EC;
  border-left-color:#F59E0B;
  padding:16px 20px;
}}
.panel blockquote.pause p{{
  color:#78350F;
  font-weight:600;
  margin:0;
}}
.panel .solo-note{{
  background:#ECFDF5;
  border-left:4px solid #10B981;
  padding:14px 18px;
  border-radius:0 var(--r-sm) var(--r-sm) 0;
  font-size:13px;
  color:#065F46;
  margin:14px 0;
}}
.panel h2.task-header{{
  background:#F7F8FA;
  border-left:4px solid var(--bc-primary);
  padding:12px 16px;
  border-radius:0 var(--r-sm) var(--r-sm) 0;
  color:var(--bc-primary);
  font-size:15px;
  margin:20px 0 12px;
}}

/* ============ TASK CARDS ============ */
.task-card{{
  background:var(--bg-white);
  border:1px solid var(--border-soft);
  border-radius:12px;
  margin:24px 0;
  overflow:hidden;
  box-shadow:0 1px 4px rgba(0,0,0,0.04);
  transition:box-shadow 0.2s;
}}
.task-card:hover{{
  box-shadow:0 3px 12px rgba(0,0,0,0.08);
}}
.task-card-header{{
  padding:16px 20px 14px;
  border-bottom:1px solid var(--border-soft);
  display:flex;
  align-items:center;
  gap:10px;
}}
.task-card-header h2{{
  margin:0;
  font-size:16px;
  font-weight:700;
  color:var(--text-dark);
  line-height:1.3;
}}
.task-card-body{{
  padding:20px 24px;
}}
.task-card-body > :first-child{{
  margin-top:0;
}}
.task-card-body > :last-child{{
  margin-bottom:0;
}}

/* Task type: regular task — purple-ish left accent */
.task-card--task{{
  border-left:4px solid var(--bc-primary);
}}
.task-card--task .task-card-header{{
  background:linear-gradient(135deg, #F9F5F7 0%, #F5F0F3 100%);
}}
.task-card--task .task-card-header h2{{
  color:var(--bc-primary);
}}
.task-card--task .task-card-header::before{{
  content:'\\1F4CB';
  font-size:18px;
}}

/* Task type: info — blue accent (väärinkäsitykset, osaamistavoitteet, CFU) */
.task-card--info{{
  border-left:4px solid #1D4ED8;
}}
.task-card--info .task-card-header{{
  background:linear-gradient(135deg, #EFF6FF 0%, #E8F0FE 100%);
}}
.task-card--info .task-card-header h2{{
  color:#1D4ED8;
}}
.task-card--info .task-card-header::before{{
  content:'\\1F4A1';
  font-size:18px;
}}

/* Task type: assessment — amber accent */
.task-card--assessment{{
  border-left:4px solid #D97706;
}}
.task-card--assessment .task-card-header{{
  background:linear-gradient(135deg, #FFFBEB 0%, #FEF3C7 100%);
}}
.task-card--assessment .task-card-header h2{{
  color:#92400E;
}}
.task-card--assessment .task-card-header::before{{
  content:'\\2B50';
  font-size:18px;
}}

/* Task type: resource — green accent */
.task-card--resource{{
  border-left:4px solid #059669;
}}
.task-card--resource .task-card-header{{
  background:linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%);
}}
.task-card--resource .task-card-header h2{{
  color:#065F46;
}}
.task-card--resource .task-card-header::before{{
  content:'\\1F4DA';
  font-size:18px;
}}

/* Remove hr separators inside card panels — cards do the separating now */
.task-card + hr,
.task-card-body hr{{
  display:none;
}}

/* Small cards (h3-level) — slightly less prominent */
.task-card--sm{{
  margin:16px 0;
  border-radius:10px;
  box-shadow:0 1px 3px rgba(0,0,0,0.03);
}}
.task-card--sm .task-card-header{{
  padding:12px 16px 10px;
}}
.task-card--sm .task-card-header h3{{
  margin:0;
  font-size:14px;
  font-weight:700;
  line-height:1.3;
}}
.task-card--sm .task-card-body{{
  padding:14px 18px;
}}
.task-card--sm .task-card-header::before{{
  font-size:15px;
}}

/* Nested h3 inside task cards (when not a card themselves) */
.task-card-body h3{{
  font-size:14px;
  font-weight:700;
  color:var(--text-dark);
  margin:18px 0 8px;
  padding-bottom:6px;
  border-bottom:1px solid #F0EDE8;
}}

/* ============ LESSON FOOTER ============ */
.lesson-footer{{
  border-top:1px solid var(--border-soft);
  padding:24px 32px;
  background:var(--bg-white);
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:16px;
}}
.nav-buttons{{
  display:flex;
  gap:12px;
}}
.btn{{
  padding:10px 20px;
  border:1px solid var(--border-soft);
  border-radius:var(--r-sm);
  background:var(--bg-white);
  color:var(--text-muted);
  font-size:13px;
  font-weight:600;
  cursor:pointer;
  transition:all 0.2s;
  display:flex;
  align-items:center;
  gap:6px;
}}
.btn:hover:not(:disabled){{
  background:rgba(105,1,59,0.05);
  color:var(--bc-primary);
  border-color:var(--bc-primary);
}}
.btn:disabled{{
  opacity:0.4;
  cursor:not-allowed;
}}
.btn-primary{{
  background:var(--bc-primary);
  color:var(--bg-white);
  border-color:var(--bc-primary);
}}
.btn-primary:hover{{
  background:var(--bc-dark);
  border-color:var(--bc-dark);
}}
.done-btn{{
  padding:10px 20px;
  border:2px solid var(--border-soft);
  border-radius:var(--r-sm);
  background:transparent;
  color:var(--text-muted);
  font-size:13px;
  font-weight:600;
  cursor:pointer;
  transition:all 0.2s;
}}
.done-btn.marked{{
  background:#ECFDF5;
  border-color:#059669;
  color:#059669;
}}
.done-btn:hover{{
  background:#ECFDF5;
  border-color:#059669;
  color:#059669;
}}

/* ============ MERMAID DIAGRAMS ============ */
.mermaid{{
  margin:32px 0;
  padding:24px 20px;
  background:linear-gradient(135deg, #FDFCFA 0%, #F5F0EB 100%);
  border:1px solid #E0D8CE;
  border-left:4px solid #69013B;
  border-radius:12px;
  text-align:center;
  overflow-x:auto;
  box-shadow:0 2px 8px rgba(105,1,59,0.06);
}}
.mermaid svg{{
  max-width:100%;
  height:auto;
  filter:saturate(0.9);
}}
/* Override mermaid node styles for BC brand */
.mermaid .node rect,
.mermaid .node circle,
.mermaid .node polygon{{
  stroke-width:1.5px !important;
  rx:8 !important;
  ry:8 !important;
}}
.mermaid .edgePath .path{{
  stroke-width:1.8px !important;
  stroke:#6B5B73 !important;
}}
.mermaid .edgeLabel{{
  font-size:13px !important;
  background:#FDFCFA !important;
  padding:2px 6px !important;
}}
.mermaid .cluster rect{{
  rx:12 !important;
  ry:12 !important;
  stroke:#C9B8D4 !important;
  fill:#F8F4FB !important;
}}
.mermaid .label{{
  font-size:14px !important;
  color:#2D2D2D !important;
}}

/* ============ RESPONSIVE ============ */
@media (max-width:768px) {{
  .topbar{{padding:12px 16px}}
  .container{{padding:40px 16px}}
  .hero-title{{font-size:32px}}
  .hero-subtitle{{font-size:15px}}
  .hero-stats{{gap:12px}}
  .osp-card-head{{padding:16px}}
  .osp-card-head,.acc-lesson{{padding-left:16px;padding-right:16px}}
  .lesson-header{{padding:24px 16px}}
  .lesson-title{{font-size:24px}}
  .lesson-panels{{padding:24px 16px}}
  .lesson-footer{{padding:16px;flex-direction:column-reverse}}
}}
</style>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<script>mermaid.initialize({{
  startOnLoad:false,
  theme:'base',
  fontFamily:'-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
  themeVariables:{{
    primaryColor:'#F3E8EE',
    primaryTextColor:'#2D2D2D',
    primaryBorderColor:'#69013B',
    lineColor:'#8B7B93',
    secondaryColor:'#EDE7F0',
    tertiaryColor:'#F0F4FF',
    noteBkgColor:'#FFF8E1',
    noteTextColor:'#2D2D2D',
    noteBorderColor:'#E0C97F',
    fontSize:'14px',
    edgeLabelBackground:'#FDFCFA'
  }}
}});</script>
</head>
<body>

<!-- TOP NAVIGATION -->
<nav class="topbar">
  <div class="logo-group">
    <div class="logo-text" onclick="showHome()">
      <span class="logo-main">Business College</span>
      <span class="logo-sub">Helsinki</span>
    </div>
    <div class="topbar-title">Tekoälyn perusteet</div>
  </div>
  <div class="topbar-right">
    <div class="progress-bar"><div class="progress-fill" id="pb"></div></div>
    <div class="progress-text" id="pt">0/27</div>
  </div>
</nav>

<!-- HOME VIEW -->
<div id="home" class="home-view">
  <div class="container">
    <div class="hero">
      <div class="hero-eyebrow">Business College Helsinki</div>
      <div class="hero-title">Tekoälyn perusteet</div>
      <div class="hero-subtitle">27 oppituntia — teoriasta käytäntöön ja agentteihin</div>
      <div class="hero-stats">
        <div class="stat-chip">
          <div class="stat-value">27</div>
          <div class="stat-label">Oppituntia</div>
        </div>
        <div class="stat-chip">
          <div class="stat-value">3</div>
          <div class="stat-label">Kokonaisuutta</div>
        </div>
        <div class="stat-chip">
          <div class="stat-value" id="done-cnt">0</div>
          <div class="stat-label">Suoritettu</div>
        </div>
      </div>
    </div>

    <!-- OSP CARDS WITH ACCORDION -->
    <div class="osp-cards">
{osp_cards_html}
    </div>

    <!-- INFO BOX -->
    <div class="info-box">
      <strong>🎬 Diat</strong> — Oppitunnin diaesitys<br><br>
      <strong>📖 Itseopiskelumateriaali</strong> — Oppitunnin sisältö<br><br>
      <strong>✏️ Opiskelutehtävät</strong> — Itsenäisesti tai pareittain tehtävät harjoitustehtävät<br><br>
      <strong>📚 Sanasto</strong> — Tunnin keskeisimmät käsitteet ja termit<br><br>
      <strong>🎓 Opettajavetoiset tehtävät</strong> — Luokassa yhdessä tehtävät harjoitukset<br><br>
      <strong>📋 Opettajan materiaali</strong> — Ohjeet ja taustatiedot tunnin pitämiseen<br><br>
      Merkitse tunti suoritetuksi valitsemalla oppitunti ja klikkaamalla "Merkitse suoritetuksi" — edistyminen tallentuu selaimeesi.
    </div>
  </div>
</div>

<!-- LESSON VIEW -->
<div id="lesson" class="lesson-view">
  <div id="lesson-header" class="lesson-header"></div>
  <div id="lesson-tabs" class="lesson-tabs"></div>
  <div id="lesson-panels" class="lesson-panels"></div>
  <div id="lesson-footer" class="lesson-footer"></div>
</div>

<script>
{js_data}
const ALLIDS={json.dumps(all_ids)};
const OSPM={osp_meta_js};
let cid=null,ctab='selfstudy';

function getDone(){{try{{return JSON.parse(localStorage.getItem('bcai-new')||'[]')}}catch{{return[]}}}}
function setDone(a){{try{{localStorage.setItem('bcai-new',JSON.stringify(a))}}catch{{}}}}
function isDone(id){{return getDone().includes(id)}}
function toggleDone(id){{const a=getDone(),i=a.indexOf(id);if(i>=0)a.splice(i,1);else a.push(id);setDone(a);updProg();updCards();updDoneBtn(id);}}
function updDoneBtn(id){{const btn=document.querySelector('.done-btn');if(!btn)return;const d=isDone(id);btn.classList.toggle('marked',d);btn.textContent=d?'✓ Suoritettu':'Merkitse suoritetuksi';}}

function updProg(){{
  const done=getDone(),n=ALLIDS.filter(id=>done.includes(id)).length;
  document.getElementById('pb').style.width=(n/ALLIDS.length*100)+'%';
  document.getElementById('pt').textContent=n+'/'+ALLIDS.length;
  const dc=document.getElementById('done-cnt');if(dc)dc.textContent=Math.round(n/ALLIDS.length*100)+'%';
}}

function updCards(){{
  const done=getDone();
  OSPM.forEach(o=>{{
    const ids=o.ids,c=ids.filter(id=>done.includes(id)).length;
    const pf=document.getElementById('pfill-'+o.id);
    const pt=document.getElementById('ptxt-'+o.id);
    if(pf)pf.style.width=(c/ids.length*100)+'%';
    if(pt)pt.textContent=c+' / '+ids.length;
    ids.forEach(id=>{{
      const btn=document.querySelector(`[onclick="loadLesson('${{id}}')"]`);
      if(!btn)return;
      btn.classList.toggle('done',done.includes(id));
      const check=btn.querySelector('[id^="done-"]');
      if(check)check.textContent=done.includes(id)?'✓':'';
    }});
  }});
}}

function toggleAcc(el){{
  const head=el;
  const lessons=head.nextElementSibling;
  head.classList.toggle('open');
  lessons.classList.toggle('open');
}}

function showHome(pushState){{
  document.getElementById('home').style.display='block';
  document.getElementById('lesson').classList.remove('active');
  cid=null;
  if(pushState!==false) history.pushState(null,'',location.pathname);
  updProg();
  window.scrollTo(0,0);
}}

function loadLesson(id,tab,pushState){{
  const d=L[id];if(!d)return;
  const defTab=(d.slides&&d.slides.length>0)?'slides':'selfstudy';
  cid=id;ctab=tab||defTab;
  document.getElementById('home').style.display='none';
  document.getElementById('lesson').classList.add('active');
  const idx=ALLIDS.indexOf(id),num=idx+1,isA=d.blockType==='assessment';
  if(pushState!==false){{
    const hash=(ctab==='selfstudy'||ctab==='slides')?'#'+id:'#'+id+'/'+ctab;
    history.pushState(null,'',hash);
  }}

  document.getElementById('lesson-header').innerHTML=`
    <div class="breadcrumb">
      <span class="bc-link" onclick="showHome()">${{d.ospIcon}} ${{d.ospTitle}}</span>
      <span>›</span>
      <span>Oppitunti ${{num}}</span>
    </div>
    <div class="lesson-title">${{d.shortTitle}}</div>
    <div class="lesson-badges">
      <span class="badge badge-osp">${{d.ospTitle}}</span>
      <span class="badge ${{isA?'badge-assess':'badge-type'}}">${{isA?'★ Arviointi':'~90 min'}}</span>
    </div>`;

  const hasSlides=d.slides&&d.slides.length>0;
  const tabs=isA
    ?[...(hasSlides?[['slides','🎬 Diat']]:[]),['selfstudy','📖 Arviointitehtävä'],['stasks','✏️ Tehtävä'],['tmats','📋 Opettajan opas']]
    :[...(hasSlides?[['slides','🎬 Diat']]:[]),['selfstudy','📖 Itseopiskelumateriaali'],['stasks','✏️ Opiskelutehtävät'],['vocab','📚 Sanasto'],['tltasks','🎓 Opettajavetoiset tehtävät'],['tmats','📋 Opettajan materiaali']];

  const tabNames=tabs.map(t=>t[0]);
  document.getElementById('lesson-tabs').innerHTML=tabs.map(([tid,lbl])=>
    `<button class="tab-btn ${{tid===ctab?'active':''}}" onclick="showTab('${{tid}}',this)">${{lbl}}</button>`
  ).join('');

  document.getElementById('lesson-panels').innerHTML=tabs.map(([tid])=>
    `<div class="panel ${{tid===ctab?'active':''}}" data-tab="${{tid}}">${{d[tid]||'<p>(Sisältöä ei ole saatavilla)</p>'}}</div>`
  ).join('');

  document.getElementById('lesson-footer').innerHTML=`
    <div class="nav-buttons">
      <button class="btn" onclick="nav(-1)" ${{idx===0?'disabled':''}}>← Edellinen</button>
      <button class="btn btn-primary" onclick="nav(1)" ${{idx===ALLIDS.length-1?'disabled':''}}>Seuraava →</button>
    </div>
    <button class="done-btn ${{isDone(id)?'marked':''}}" onclick="toggleDone('${{id}}')">
      ${{isDone(id)?'✓ Suoritettu':'Merkitse suoritetuksi'}}
    </button>`;
  window.scrollTo(0,0);
  mermaid.run({{querySelector:'.panel.active .mermaid'}});
}}

function showTab(name,btn,pushState){{
  ctab=name;
  document.querySelectorAll('.panel').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(t=>t.classList.remove('active'));
  const panels=document.querySelectorAll('.panel');
  const tabs=document.querySelectorAll('.tab-btn');
  if(btn){{
    const tabIdx=Array.from(tabs).indexOf(btn);
    if(tabIdx>=0&&panels[tabIdx]){{
      panels[tabIdx].classList.add('active');
      btn.classList.add('active');
    }}
  }}else{{
    // Find tab by name (for hash navigation)
    const panel=document.querySelector(`.panel[data-tab="${{name}}"]`);
    if(panel)panel.classList.add('active');
    const tabBtns=Array.from(tabs);
    const panelArr=Array.from(panels);
    const pi=panelArr.indexOf(panel);
    if(pi>=0&&tabBtns[pi])tabBtns[pi].classList.add('active');
  }}
  if(pushState!==false&&cid){{
    const hash=(name==='selfstudy'||name==='slides')?'#'+cid:'#'+cid+'/'+name;
    history.pushState(null,'',hash);
  }}
  document.getElementById('lesson-panels').scrollTop=0;
  mermaid.run({{querySelector:'.panel.active .mermaid'}});
}}

function nav(dir){{
  const i=ALLIDS.indexOf(cid),next=ALLIDS[i+dir];
  if(next)loadLesson(next);
}}

function routeFromHash(pushState){{
  const h=location.hash.replace('#','');
  if(!h){{ showHome(false); return; }}
  const parts=h.split('/');
  const lid=parts[0],tab=parts[1]||'selfstudy';
  if(L[lid]){{ loadLesson(lid,tab,pushState===true?true:false); }}
  else{{ showHome(false); }}
}}

window.addEventListener('popstate',()=>routeFromHash(false));

// Initial route from hash on page load
updProg();updCards();
routeFromHash(false);
</script>

</body>
</html>'''


if __name__ == '__main__':
    print("Reading lesson content...")
    data = build_lesson_data()
    print(f"Loaded {len(data)} lessons")
    print("Generating HTML...")
    out = generate_html(data)
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(out)
    size_kb = os.path.getsize(OUT) // 1024
    print(f"Written: {OUT}")
    print(f"Size: {size_kb} KB")
