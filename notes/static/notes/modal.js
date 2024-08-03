document.addEventListener('DOMContentLoaded', function(){
    const pdfModal = new bootstrap.Modal(document.getElementById('pdfModal'));
    const pdfEmbed = document.getElementById('pdfEmbed');
    const modalHeading = document.getElementById('modalLabel')
    const modalDownloadBtn = document.getElementById('modalDownloadBtn')
    document.querySelectorAll('.note-title').forEach(title => {
        title.addEventListener('click', function(event){
            const pdfUrl = this.dataset.noteFile;
            modalHeading.innerText = `${this.innerText} - Preview`
            modalDownloadBtn.href = this.dataset.noteFile
            pdfEmbed.src = pdfUrl;
            pdfModal.show();

        })
    })

})