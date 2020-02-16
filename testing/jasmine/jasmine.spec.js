describe('Testing - ', () => {

    it ('openSearchBar should increase width to 100%', function() {
        $(".content").append("<div id='overlaySearchBar' style='width:10%'></div>");
        let searchBar = document.getElementById("overlaySearchBar");
        expect(searchBar.style.width).toEqual('10%')
        openSearchBar();
        expect(searchBar.style.width).toEqual('100%')
    });
});
